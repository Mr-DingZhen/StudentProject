CREATE
    DATABASE student_info CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE student_info;
CREATE TABLE admin
(
    id       INT AUTO_INCREMENT PRIMARY KEY COMMENT '管理员ID',
    username VARCHAR(255) NOT NULL COMMENT '账号',
    password VARCHAR(255) NOT NULL COMMENT '密码',
    name     VARCHAR(255) NULL COMMENT '姓名',
    role     VARCHAR(255) NULL COMMENT '角色'
) COMMENT '管理员表' ENGINE = InnoDB;

CREATE TABLE course
(
    id          INT AUTO_INCREMENT PRIMARY KEY COMMENT '课程ID',
    name        VARCHAR(255) NULL COMMENT '课程名称',
    number      VARCHAR(255) NULL COMMENT '课程编号',
    description VARCHAR(255) NULL COMMENT '课程描述',
    periods     VARCHAR(255) NULL COMMENT '课时',
    teacher     VARCHAR(255) NULL COMMENT '任课老师'
) COMMENT '课程信息' ENGINE = InnoDB;



CREATE TABLE student
(
    id       INT AUTO_INCREMENT PRIMARY KEY COMMENT '学生表主键ID',
    username VARCHAR(255) NOT NULL COMMENT '学号/用户名',
    password VARCHAR(255) NOT NULL COMMENT '密码',
    name     VARCHAR(255) NOT NULL COMMENT '学生姓名',
    gender   VARCHAR(10)  NULL COMMENT '性别',
    phone    VARCHAR(255) NULL COMMENT '手机号',
    birthday VARCHAR(255) NULL COMMENT '出生日期',
    avatar   VARCHAR(255) NULL COMMENT '头像',
    role     VARCHAR(255) NULL COMMENT '用户角色',
    UNIQUE (username) COMMENT '学号/用户名唯一'
) COMMENT '学生信息' ENGINE = InnoDB;

CREATE TABLE student_course
(
    id         INT AUTO_INCREMENT PRIMARY KEY COMMENT '选课表主键ID',
    name       VARCHAR(255) NULL COMMENT '课程名称',
    number     VARCHAR(255) NULL COMMENT '课程编号',
    student_id INT          NULL COMMENT '学生ID',
    course_id  INT          NULL COMMENT '课程ID',
    FOREIGN KEY (student_id) REFERENCES student (id),
    FOREIGN KEY (course_id) REFERENCES course (id)
) COMMENT '学生选课表' ENGINE = InnoDB;

CREATE TABLE grade
(
    id         INT AUTO_INCREMENT PRIMARY KEY COMMENT '学生成绩表主键ID',
    course_id  INT           NULL COMMENT '课程ID',
    student_id INT           NULL COMMENT '学生ID',
    score      DOUBLE(10, 1) NULL COMMENT '成绩',
    comment    VARCHAR(255)  NULL COMMENT '教师评语',
    feedback   VARCHAR(255)  NULL COMMENT '学生评价',
    FOREIGN KEY (course_id) REFERENCES course (id),
    FOREIGN KEY (student_id) REFERENCES student (id)
) COMMENT '学生成绩表' ENGINE = InnoDB;


INSERT INTO admin (username, password, name, role)
VALUES ('admin', '$2b$12$9Yidy/B7g8pJFL8K4UY9n.1yneDTAdvZKn/El0oaMIl1vixK/bQ9a', 'admin', 'ADMIN');
