"""Seed the database with initial data from existing site content."""
import json
import sys
from app import create_app
from models import db, Teacher, Testimonial, SiteContent

app = create_app()

with app.app_context():
    db.create_all()

    # ── Teachers ──
    if Teacher.query.count() == 0:
        teachers = [
            Teacher(
                name="刘老师",
                slug="liu-laoshi",
                avatar="images/001.jpg",
                education="山东师范大学 毕业",
                experience="教龄 4 年",
                subjects=json.dumps(["小学全科", "初中全科", "高中数学", "高中英语", "高中物理", "高中化学", "考前冲刺"]),
                grade_levels=json.dumps(["primary", "middle", "high"]),
                special_badge="数学 · 物理",
                sort_order=1,
                bio="刘老师，山东师范大学毕业，4年教学经验。擅长小学全科、初中全科、高中数学/英语/物理/化学教学，对考前冲刺有丰富经验。教学风格耐心细致，善于发现学生的薄弱环节并针对性辅导。",
            ),
            Teacher(
                name="邸老师",
                slug="di-laoshi",
                avatar="images/di.jpg",
                education="青岛大学 毕业",
                experience="教龄 3 年",
                subjects=json.dumps(["小学英语", "初中英语", "高中英语", "初中数学", "初中物理", "高中数学"]),
                grade_levels=json.dumps(["primary", "middle", "high"]),
                special_badge="英语专项",
                sort_order=2,
                bio="邸老师，青岛大学毕业，3年教学经验。英语专项能力强，同时可辅导初中数学和物理。教学方式灵活，能根据学生特点调整教学节奏，深受学生喜爱。",
            ),
            Teacher(
                name="张老师",
                slug="zhang-laoshi",
                avatar="",
                education="山东大学 数学系 本科",
                experience="",
                subjects=json.dumps(["初中数学", "高中数学", "中考冲刺", "高考冲刺"]),
                grade_levels=json.dumps(["middle", "high"]),
                sort_order=3,
                is_placeholder=True,
                bio="",
            ),
            Teacher(
                name="李老师",
                slug="li-laoshi",
                avatar="",
                education="山东师范大学 物理系 研究生",
                experience="",
                subjects=json.dumps(["初中物理", "高中物理", "高中化学", "实验专项"]),
                grade_levels=json.dumps(["middle", "high"]),
                sort_order=4,
                is_placeholder=True,
                bio="",
            ),
            Teacher(
                name="赵老师",
                slug="zhao-laoshi",
                avatar="",
                education="师范院校 汉语言文学专业 本科",
                experience="",
                subjects=json.dumps(["小学语文", "初中语文", "阅读专项", "作文辅导"]),
                grade_levels=json.dumps(["primary", "middle"]),
                sort_order=5,
                is_placeholder=True,
                bio="",
            ),
            Teacher(
                name="陈老师",
                slug="chen-laoshi",
                avatar="",
                education="中国海洋大学 化学工程 研究生",
                experience="",
                subjects=json.dumps(["初中数学", "初中化学", "高中化学", "生物基础"]),
                grade_levels=json.dumps(["middle", "high"]),
                sort_order=6,
                is_placeholder=True,
                bio="",
            ),
        ]
        db.session.add_all(teachers)
        print(f"  ✓ Seeded {len(teachers)} teachers")

    # ── Testimonials ──
    if Testimonial.query.count() == 0:
        testimonials = [
            Testimonial(
                author="王同学妈妈",
                content="孩子初二数学一直在及格线徘徊，跟着刘老师辅导了两个月，期中考试考了 87 分。老师很负责，每次课后都会跟我们沟通情况。",
                student_grade="初二",
                subject="数学",
                improvement="数学 60→87",
                sort_order=1,
            ),
            Testimonial(
                author="李同学家长",
                content="高三英语特别差，邸老师针对高考考点给娃做了专项训练，三个月提了 30 多分。孩子说邸老师讲得比学校老师还清楚。",
                student_grade="高三",
                subject="英语",
                improvement="英语 70→103",
                sort_order=2,
            ),
            Testimonial(
                author="张同学爸爸",
                content="小学四年级，之前作业拖拉严重。老师上门辅导后，不仅作业完成快了，成绩也从班级中下游到了前十。上门辅导确实省心。",
                student_grade="四年级",
                subject="全科",
                improvement="班级进步 15+ 名",
                sort_order=3,
            ),
            Testimonial(
                author="赵同学妈妈",
                content="高一物理跟不上，李老师（待上线）是山师物理系研究生，讲得特别系统。试听了一节课孩子就说想继续上，现在物理稳定在 80 以上。",
                student_grade="高一",
                subject="物理",
                improvement="物理 45→82",
                sort_order=4,
            ),
        ]
        db.session.add_all(testimonials)
        print(f"  ✓ Seeded {len(testimonials)} testimonials")

    # ── Site Content ──
    if SiteContent.query.count() == 0:
        contents = [
            SiteContent(page="home", section="hero", key="title", content="思贤家教"),
            SiteContent(page="home", section="hero", key="subtitle", content="济南商河 · 本地上门辅导"),
            SiteContent(page="home", section="hero", key="description", content="让每个孩子都能找到合适的老师"),
            SiteContent(page="home", section="about", key="text_1", content='我们是来自<span class="highlight">商河县</span>的一群家教老师，专注于中小学上门一对一辅导。以"让每个孩子都能找到合适的老师"为目标，致力于为商河家庭提供优质、便捷、个性化的辅导服务。'),
            SiteContent(page="home", section="about", key="text_2", content='我们采用<span class="highlight">上门辅导</span>模式，省去家长接送奔波，让孩子在熟悉的环境中高效学习。没有中间环节，课时费更合理，让家长把费用花在教学质量上。'),
            SiteContent(page="home", section="about", key="text_3", content='目前我们有多位经验丰富的合作老师，涵盖小学至高中各学科。每位老师都具备扎实的学科功底和良好的教学能力。'),
            SiteContent(page="home", section="cta", key="title", content="免费试听一节课"),
            SiteContent(page="home", section="cta", key="description", content="先体验，满意再报名"),
        ]
        db.session.add_all(contents)
        print(f"  ✓ Seeded {len(contents)} site contents")

    db.session.commit()
    print("\n✅ Database seeded successfully!")
