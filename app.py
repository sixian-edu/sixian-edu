import os
import functools
import json
from pathlib import Path
from flask import (
    Flask, render_template, request, redirect, url_for,
    session, flash, abort, jsonify, send_from_directory,
)
from dotenv import load_dotenv

load_dotenv()


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object("config.Config")
    app.config["PROJECT_ROOT"] = Path(__file__).parent

    # Serve images/ and css/ from project root (alongside Flask's static/)
    @app.route("/images/<path:filename>")
    def serve_images(filename):
        return send_from_directory(app.config["PROJECT_ROOT"] / "images", filename)

    @app.route("/css/<path:filename>")
    def serve_css(filename):
        return send_from_directory(app.config["PROJECT_ROOT"] / "css", filename)

    @app.route("/favicon.ico")
    def favicon():
        return send_from_directory(app.config["PROJECT_ROOT"] / "images", "favicon.png")

    if test_config:
        app.config.update(test_config)

    from models import db
    db.init_app(app)

    with app.app_context():
        from models import Teacher, Booking, Testimonial, SiteContent
        db.create_all()
        # Auto-seed if database is empty
        if Teacher.query.count() == 0:
            _auto_seed()

    # ── Helpers ──

    def login_required(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            if not session.get("admin_logged_in"):
                return redirect(url_for("admin_login"))
            return f(*args, **kwargs)
        return wrapper

    # ── Auto-seed ──

    def _auto_seed():
        """Seed initial data on first run."""
        import json
        from models import Teacher, Testimonial, SiteContent

        teachers = [
            Teacher(name="刘老师", slug="liu-laoshi", avatar="images/001.jpg",
                    education="山东师范大学 毕业", experience="教龄 4 年",
                    subjects=json.dumps(["小学全科", "初中全科", "高中数学", "高中英语", "高中物理", "高中化学", "考前冲刺"]),
                    grade_levels=json.dumps(["primary", "middle", "high"]), special_badge="数学 · 物理", sort_order=1,
                    bio="刘老师，山东师范大学毕业，4年教学经验。擅长小学全科、初中全科、高中数学/英语/物理/化学教学，对考前冲刺有丰富经验。教学风格耐心细致，善于发现学生的薄弱环节并针对性辅导。"),
            Teacher(name="邸老师", slug="di-laoshi", avatar="images/di.jpg",
                    education="青岛大学 毕业", experience="教龄 3 年",
                    subjects=json.dumps(["小学英语", "初中英语", "高中英语", "初中数学", "初中物理", "高中数学"]),
                    grade_levels=json.dumps(["primary", "middle", "high"]), special_badge="英语专项", sort_order=2,
                    bio="邸老师，青岛大学毕业，3年教学经验。英语专项能力强，同时可辅导初中数学和物理。教学方式灵活，能根据学生特点调整教学节奏，深受学生喜爱。"),
            Teacher(name="张老师", slug="zhang-laoshi", education="山东大学 数学系 本科",
                    subjects=json.dumps(["初中数学", "高中数学", "中考冲刺", "高考冲刺"]),
                    grade_levels=json.dumps(["middle", "high"]), sort_order=3, is_placeholder=True),
            Teacher(name="李老师", slug="li-laoshi", education="山东师范大学 物理系 研究生",
                    subjects=json.dumps(["初中物理", "高中物理", "高中化学", "实验专项"]),
                    grade_levels=json.dumps(["middle", "high"]), sort_order=4, is_placeholder=True),
            Teacher(name="赵老师", slug="zhao-laoshi", education="师范院校 汉语言文学专业 本科",
                    subjects=json.dumps(["小学语文", "初中语文", "阅读专项", "作文辅导"]),
                    grade_levels=json.dumps(["primary", "middle"]), sort_order=5, is_placeholder=True),
            Teacher(name="陈老师", slug="chen-laoshi", education="中国海洋大学 化学工程 研究生",
                    subjects=json.dumps(["初中数学", "初中化学", "高中化学", "生物基础"]),
                    grade_levels=json.dumps(["middle", "high"]), sort_order=6, is_placeholder=True),
        ]
        db.session.add_all(teachers)

        testimonials = [
            Testimonial(author="王同学妈妈", sort_order=1,
                        content="孩子初二数学一直在及格线徘徊，跟着刘老师辅导了两个月，期中考试考了 87 分。老师很负责，每次课后都会跟我们沟通情况。",
                        improvement="数学 60→87"),
            Testimonial(author="李同学家长", sort_order=2,
                        content="高三英语特别差，邸老师针对高考考点给娃做了专项训练，三个月提了 30 多分。孩子说邸老师讲得比学校老师还清楚。",
                        improvement="英语 70→103"),
            Testimonial(author="张同学爸爸", sort_order=3,
                        content="小学四年级，之前作业拖拉严重。老师上门辅导后，不仅作业完成快了，成绩也从班级中下游到了前十。上门辅导确实省心。",
                        improvement="班级进步 15+ 名"),
            Testimonial(author="赵同学妈妈", sort_order=4,
                        content="高一物理跟不上，李老师是山师物理系研究生，讲得特别系统。试听了一节课孩子就说想继续上，现在物理稳定在 80 以上。",
                        improvement="物理 45→82"),
        ]
        db.session.add_all(testimonials)

        contents = [
            SiteContent(page="home", section="hero", key="title", content="思贤家教"),
            SiteContent(page="home", section="hero", key="subtitle", content="济南商河 · 本地上门辅导"),
            SiteContent(page="home", section="hero", key="description", content="让每个孩子都能找到合适的老师"),
            SiteContent(page="home", section="about", key="text_1",
                        content='我们是来自<span class="highlight">商河县</span>的一群家教老师，专注于中小学上门一对一辅导。以"让每个孩子都能找到合适的老师"为目标，致力于为商河家庭提供优质、便捷、个性化的辅导服务。'),
            SiteContent(page="home", section="about", key="text_2",
                        content='我们采用<span class="highlight">上门辅导</span>模式，省去家长接送奔波，让孩子在熟悉的环境中高效学习。没有中间环节，课时费更合理，让家长把费用花在教学质量上。'),
            SiteContent(page="home", section="about", key="text_3",
                        content='目前我们有多位经验丰富的合作老师，涵盖小学至高中各学科。每位老师都具备扎实的学科功底和良好的教学能力。'),
            SiteContent(page="home", section="cta", key="title", content="免费试听一节课"),
            SiteContent(page="home", section="cta", key="description", content="先体验，满意再报名"),
        ]
        db.session.add_all(contents)
        db.session.commit()
        print("✅ Database auto-seeded")

    # ── Public Routes ──

    @app.route("/")
    def home():
        from models import Testimonial, SiteContent
        testimonials = Testimonial.query.filter_by(is_active=True).order_by(Testimonial.sort_order).all()
        contents = SiteContent.query.all()
        content_map = {}
        for c in contents:
            content_map[f"{c.page}_{c.section}_{c.key}"] = c.content
        return render_template("index.html", testimonials=testimonials, content=content_map)

    @app.route("/teachers")
    def teachers():
        from models import Teacher
        all_teachers = Teacher.query.filter_by(is_active=True).order_by(Teacher.sort_order).all()
        return render_template("teachers.html", teachers=all_teachers)

    @app.route("/teachers/<slug>")
    def teacher_detail(slug):
        from models import Teacher
        teacher = Teacher.query.filter_by(slug=slug, is_active=True).first_or_404()
        return render_template("teacher_detail.html", teacher=teacher)

    @app.route("/booking", methods=["GET", "POST"])
    def booking():
        from models import Booking
        if request.method == "POST":
            booking = Booking(
                parent_name=request.form.get("parent_name", ""),
                phone=request.form.get("phone", ""),
                grade=request.form.get("grade", ""),
                subject=request.form.get("subject", ""),
                notes=request.form.get("notes", ""),
            )
            db.session.add(booking)
            db.session.commit()

            # Also forward to Web3Forms as before
            return render_template("booking.html", submitted=True)

        return render_template("booking.html", submitted=False)

    @app.route("/algo")
    def algo():
        return render_template("algo.html")

    @app.route("/exam-papers")
    def exam_papers():
        return render_template("exam_papers.html")

    @app.route("/join")
    def join():
        return render_template("join.html")

    @app.route("/covenant")
    def covenant():
        return render_template("covenant.html")

    @app.route("/api/submit-booking", methods=["POST"])
    def api_submit_booking():
        from models import Booking
        data = request.get_json()
        if not data:
            return jsonify({"success": False, "message": "Invalid data"}), 400

        booking = Booking(
            parent_name=data.get("name", ""),
            phone=data.get("phone", ""),
            grade=data.get("grade", ""),
            subject=data.get("subject", ""),
            notes=data.get("notes", ""),
        )
        db.session.add(booking)
        db.session.commit()
        return jsonify({"success": True})

    # ── Admin Routes ──

    @app.route("/admin/login", methods=["GET", "POST"])
    def admin_login():
        if request.method == "POST":
            pwd = request.form.get("password", "")
            if pwd == app.config["ADMIN_PASSWORD"]:
                session["admin_logged_in"] = True
                session.permanent = True
                return redirect(url_for("admin_dashboard"))
            flash("密码错误", "error")
        return render_template("admin/login.html")

    @app.route("/admin/logout")
    def admin_logout():
        session.pop("admin_logged_in", None)
        return redirect(url_for("admin_login"))

    @app.route("/admin")
    @login_required
    def admin_dashboard():
        from models import Teacher, Booking, Testimonial
        teacher_count = Teacher.query.count()
        pending_bookings = Booking.query.filter_by(status="pending").count()
        total_bookings = Booking.query.count()
        testimonial_count = Testimonial.query.count()
        latest_bookings = Booking.query.order_by(Booking.created_at.desc()).limit(5).all()
        return render_template(
            "admin/dashboard.html",
            teacher_count=teacher_count,
            pending_bookings=pending_bookings,
            total_bookings=total_bookings,
            testimonial_count=testimonial_count,
            latest_bookings=latest_bookings,
        )

    # ── Admin: Teachers ──

    @app.route("/admin/teachers")
    @login_required
    def admin_teachers():
        from models import Teacher
        all_teachers = Teacher.query.order_by(Teacher.sort_order).all()
        return render_template("admin/teachers.html", teachers=all_teachers)

    @app.route("/admin/teachers/new", methods=["GET", "POST"])
    @login_required
    def admin_teacher_new():
        from models import Teacher
        if request.method == "POST":
            teacher = Teacher(
                name=request.form["name"],
                slug=request.form["slug"],
                avatar=request.form.get("avatar", ""),
                education=request.form.get("education", ""),
                experience=request.form.get("experience", ""),
                bio=request.form.get("bio", ""),
                subjects=json.dumps(request.form.getlist("subjects")),
                grade_levels=json.dumps(request.form.getlist("grade_levels")),
                special_badge=request.form.get("special_badge", ""),
                is_placeholder=request.form.get("is_placeholder") == "on",
                is_active=request.form.get("is_active") == "on",
                sort_order=int(request.form.get("sort_order", 0)),
            )
            db.session.add(teacher)
            db.session.commit()
            flash("老师添加成功", "success")
            return redirect(url_for("admin_teachers"))
        return render_template("admin/teacher_form.html", teacher=None)

    @app.route("/admin/teachers/<int:id>/edit", methods=["GET", "POST"])
    @login_required
    def admin_teacher_edit(id):
        from models import Teacher
        teacher = Teacher.query.get_or_404(id)
        if request.method == "POST":
            teacher.name = request.form["name"]
            teacher.slug = request.form["slug"]
            teacher.avatar = request.form.get("avatar", "")
            teacher.education = request.form.get("education", "")
            teacher.experience = request.form.get("experience", "")
            teacher.bio = request.form.get("bio", "")
            teacher.subjects = json.dumps(request.form.getlist("subjects"))
            teacher.grade_levels = json.dumps(request.form.getlist("grade_levels"))
            teacher.special_badge = request.form.get("special_badge", "")
            teacher.is_placeholder = request.form.get("is_placeholder") == "on"
            teacher.is_active = request.form.get("is_active") == "on"
            teacher.sort_order = int(request.form.get("sort_order", 0))
            db.session.commit()
            flash("老师信息已更新", "success")
            return redirect(url_for("admin_teachers"))
        return render_template("admin/teacher_form.html", teacher=teacher)

    @app.route("/admin/teachers/<int:id>/delete", methods=["POST"])
    @login_required
    def admin_teacher_delete(id):
        from models import Teacher
        teacher = Teacher.query.get_or_404(id)
        db.session.delete(teacher)
        db.session.commit()
        flash("老师已删除", "success")
        return redirect(url_for("admin_teachers"))

    # ── Admin: Bookings ──

    @app.route("/admin/bookings")
    @login_required
    def admin_bookings():
        from models import Booking
        status_filter = request.args.get("status", "all")
        query = Booking.query
        if status_filter != "all":
            query = query.filter_by(status=status_filter)
        all_bookings = query.order_by(Booking.created_at.desc()).all()
        return render_template("admin/bookings.html", bookings=all_bookings, current_filter=status_filter)

    @app.route("/admin/bookings/<int:id>/status", methods=["POST"])
    @login_required
    def admin_booking_status(id):
        from models import Booking
        booking = Booking.query.get_or_404(id)
        new_status = request.form.get("status", "pending")
        if new_status in ("pending", "confirmed", "completed", "cancelled"):
            booking.status = new_status
            db.session.commit()
        return redirect(url_for("admin_bookings"))

    # ── Admin: Testimonials ──

    @app.route("/admin/testimonials")
    @login_required
    def admin_testimonials():
        from models import Testimonial
        all_testimonials = Testimonial.query.order_by(Testimonial.sort_order).all()
        return render_template("admin/testimonials.html", testimonials=all_testimonials)

    @app.route("/admin/testimonials/new", methods=["GET", "POST"])
    @login_required
    def admin_testimonial_new():
        from models import Testimonial
        if request.method == "POST":
            t = Testimonial(
                author=request.form.get("author", ""),
                content=request.form["content"],
                student_grade=request.form.get("student_grade", ""),
                subject=request.form.get("subject", ""),
                improvement=request.form.get("improvement", ""),
                is_active=request.form.get("is_active") == "on",
                sort_order=int(request.form.get("sort_order", 0)),
            )
            db.session.add(t)
            db.session.commit()
            flash("评价添加成功", "success")
            return redirect(url_for("admin_testimonials"))
        return render_template("admin/testimonial_form.html", testimonial=None)

    @app.route("/admin/testimonials/<int:id>/edit", methods=["GET", "POST"])
    @login_required
    def admin_testimonial_edit(id):
        from models import Testimonial
        t = Testimonial.query.get_or_404(id)
        if request.method == "POST":
            t.author = request.form.get("author", "")
            t.content = request.form["content"]
            t.student_grade = request.form.get("student_grade", "")
            t.subject = request.form.get("subject", "")
            t.improvement = request.form.get("improvement", "")
            t.is_active = request.form.get("is_active") == "on"
            t.sort_order = int(request.form.get("sort_order", 0))
            db.session.commit()
            flash("评价已更新", "success")
            return redirect(url_for("admin_testimonials"))
        return render_template("admin/testimonial_form.html", testimonial=t)

    @app.route("/admin/testimonials/<int:id>/delete", methods=["POST"])
    @login_required
    def admin_testimonial_delete(id):
        from models import Testimonial
        t = Testimonial.query.get_or_404(id)
        db.session.delete(t)
        db.session.commit()
        flash("评价已删除", "success")
        return redirect(url_for("admin_testimonials"))

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
