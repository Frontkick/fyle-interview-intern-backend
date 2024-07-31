CREATE SEQUENCE assignments_id_seq;

CREATE TABLE assignments (
    id INTEGER DEFAULT nextval('assignments_id_seq') PRIMARY KEY,
    student_id INTEGER NOT NULL,
    teacher_id INTEGER,
    content TEXT,
    grade VARCHAR(255), -- or another appropriate length/enum type if GradeEnum is defined
    state VARCHAR(255) DEFAULT 'DRAFT' NOT NULL, -- or another appropriate length/enum type if AssignmentStateEnum is defined
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (teacher_id) REFERENCES teachers(id)
);

-- To handle updates, you might need to use a trigger or application logic, as PostgreSQL doesn't support on-update directly.

-- Create the sequence for the id column
CREATE SEQUENCE principals_id_seq;

-- Create the principals table
CREATE TABLE principals (
    id INTEGER DEFAULT nextval('principals_id_seq') PRIMARY KEY,
    user_id INTEGER,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Note: PostgreSQL does not support the `onupdate` directly for timestamps. 
-- You will need to use a trigger or application logic to handle the automatic update of the `updated_at` field.
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = now();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_principal_timestamp
BEFORE UPDATE ON principals
FOR EACH ROW
EXECUTE FUNCTION update_timestamp();


-- Create the sequence for the id column
CREATE SEQUENCE students_id_seq;

-- Create the students table
CREATE TABLE students (
    id INTEGER DEFAULT nextval('students_id_seq') PRIMARY KEY,
    user_id INTEGER,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Note: PostgreSQL does not support the `onupdate` directly for timestamps. 
-- You will need to use a trigger or application logic to handle the automatic update of the `updated_at` field.
CREATE OR REPLACE FUNCTION update_student_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = now();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_student_timestamp_trigger
BEFORE UPDATE ON students
FOR EACH ROW
EXECUTE FUNCTION update_student_timestamp();


-- Create the sequence for the id column
CREATE SEQUENCE teachers_id_seq;

-- Create the teachers table
CREATE TABLE teachers (
    id INTEGER DEFAULT nextval('teachers_id_seq') PRIMARY KEY,
    user_id INTEGER,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Note: PostgreSQL does not support the `onupdate` directly for timestamps. 
-- You will need to use a trigger or application logic to handle the automatic update of the `updated_at` field.



CREATE OR REPLACE FUNCTION update_teacher_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = now();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_teacher_timestamp_trigger
BEFORE UPDATE ON teachers
FOR EACH ROW
EXECUTE FUNCTION update_teacher_timestamp();


-- Create the sequence for the id column
CREATE SEQUENCE users_id_seq;

-- Create the users table
CREATE TABLE users (
    id INTEGER DEFAULT nextval('users_id_seq') PRIMARY KEY,
    username VARCHAR(80) UNIQUE NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now() NOT NULL
);

-- Note: PostgreSQL does not support the `onupdate` directly for timestamps. 
-- You will need to use a trigger or application logic to handle the automatic update of the `updated_at` field.

CREATE OR REPLACE FUNCTION update_user_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = now();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_user_timestamp_trigger
BEFORE UPDATE ON users
FOR EACH ROW
EXECUTE FUNCTION update_user_timestamp();
