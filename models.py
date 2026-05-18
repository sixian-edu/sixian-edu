import json
from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Teacher(db.Model):
    __tablename__ = "teachers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    slug = db.Column(db.String(50), unique=True, nullable=False)
    avatar = db.Column(db.String(200), default="")
    education = db.Column(db.String(200), default="")
    experience = db.Column(db.String(100), default="")  # e.g. "教龄 4 年"
    bio = db.Column(db.Text, default="")
    subjects = db.Column(db.Text, default="[]")  # JSON array
    grade_levels = db.Column(db.Text, default="[]")  # JSON array
    special_badge = db.Column(db.String(100), default="")
    is_active = db.Column(db.Boolean, default=True)
    sort_order = db.Column(db.Integer, default=0)
    is_placeholder = db.Column(db.Boolean, default=False)
    created_at = db.Column(
        db.DateTime, default=lambda: datetime.now(timezone.utc)
    )

    def subject_list(self):
        return json.loads(self.subjects) if self.subjects else []

    def grade_list(self):
        return json.loads(self.grade_levels) if self.grade_levels else []

    def detail_url(self):
        return f"/teachers/{self.slug}"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "slug": self.slug,
            "avatar": self.avatar,
            "education": self.education,
            "experience": self.experience,
            "bio": self.bio,
            "subjects": self.subject_list(),
            "grade_levels": self.grade_list(),
            "special_badge": self.special_badge,
            "is_active": self.is_active,
            "sort_order": self.sort_order,
            "is_placeholder": self.is_placeholder,
        }


class Booking(db.Model):
    __tablename__ = "bookings"

    id = db.Column(db.Integer, primary_key=True)
    parent_name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    grade = db.Column(db.String(20), default="")
    subject = db.Column(db.String(100), default="")
    notes = db.Column(db.Text, default="")
    status = db.Column(db.String(20), default="pending")  # pending/confirmed/completed/cancelled
    created_at = db.Column(
        db.DateTime, default=lambda: datetime.now(timezone.utc)
    )

    def to_dict(self):
        return {
            "id": self.id,
            "parent_name": self.parent_name,
            "phone": self.phone,
            "grade": self.grade,
            "subject": self.subject,
            "notes": self.notes,
            "status": self.status,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M"),
        }


class Testimonial(db.Model):
    __tablename__ = "testimonials"

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(50), default="")  # e.g. "王同学妈妈"
    content = db.Column(db.Text, nullable=False)
    student_grade = db.Column(db.String(20), default="")
    subject = db.Column(db.String(100), default="")
    improvement = db.Column(db.String(200), default="")  # e.g. "数学 65→92"
    is_active = db.Column(db.Boolean, default=True)
    sort_order = db.Column(db.Integer, default=0)
    created_at = db.Column(
        db.DateTime, default=lambda: datetime.now(timezone.utc)
    )

    def to_dict(self):
        return {
            "id": self.id,
            "author": self.author,
            "content": self.content,
            "student_grade": self.student_grade,
            "subject": self.subject,
            "improvement": self.improvement,
            "is_active": self.is_active,
        }


class SiteContent(db.Model):
    __tablename__ = "site_content"

    id = db.Column(db.Integer, primary_key=True)
    page = db.Column(db.String(50), nullable=False)
    section = db.Column(db.String(50), nullable=False)
    key = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, default="")
    updated_at = db.Column(
        db.DateTime, default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    __table_args__ = (
        db.UniqueConstraint("page", "section", "key"),
    )
