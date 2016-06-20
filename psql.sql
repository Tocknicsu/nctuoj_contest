DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS execute_types CASCADE;
DROP TABLE IF EXISTS execute_steps CASCADE;
CREATE OR REPLACE FUNCTION updated_row() 
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = date_trunc('second', now());
    RETURN NEW; 
END;
$$ language 'plpgsql';

-- CREATE TABLE table_name (
    --     id              serial          NOT NULL    PRIMARY KEY,
    --     created_at      timestamp       DEFAULT now(),
    --     updated_at      timestamp       DEFAULT now()
    -- );
-- CREATE TRIGGER table_name_updated_at_column BEFORE UPDATE ON table_name FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column_column();

CREATE TABLE users (
    id              serial          NOT NULL    PRIMARY KEY,
    account         varchar(32)     NOT NULL,
    password        varchar(32)     NOT NULL,
    token           varchar(64)     NOT NULL,
    created_at      timestamp       DEFAULT date_trunc('second', now()),
    updated_at      timestamp       DEFAULT date_trunc('second', now())
);
CREATE TRIGGER users_updated_row BEFORE UPDATE ON users FOR EACH ROW EXECUTE PROCEDURE updated_row();
CREATE UNIQUE INDEX on users (token);
CREATE UNIQUE INDEX on users (account);
INSERT INTO users (account, password, token) VALUES ('admin', '21232f297a57a5a743894a0e4a801fc3', 'ADMIN@TOKEN');


CREATE TABLE execute_types (
    id              serial          NOT NULL    PRIMARY KEY,
    description     varchar(255)    NOT NULL    DEFAULT '',
    priority        integer         NOT NULL    DEFAULT 999,
    created_at      timestamp       DEFAULT date_trunc('second',now()),
    updated_at      timestamp       DEFAULT date_trunc('second',now())
);
CREATE TRIGGER execute_types_updated_row BEFORE UPDATE ON execute_types FOR EACH ROW EXECUTE PROCEDURE updated_row();
CREATE INDEX on execute_types (priority);
INSERT INTO execute_types (description, priority) values ('C', 1);
INSERT INTO execute_types (description, priority) values ('C++', 2);
INSERT INTO execute_types (description, priority) values ('C++11', 3);
INSERT INTO execute_types (description, priority) values ('Java', 4);
INSERT INTO execute_types (description, priority) values ('Python2', 5);
INSERT INTO execute_types (description, priority) values ('Python3', 6);

CREATE TABLE execute_steps (
    id              serial          NOT NULL    PRIMARY KEY,
    execute_type_id integer         NOT NULL    REFERENCES execute_types(id)    ON DELETE CASCADE,
    command         varchar(255)    NOT NULL    DEFAULT '',
    created_at      timestamp       DEFAULT date_trunc('second',now()),
    updated_at      timestamp       DEFAULT date_trunc('second',now())
);
CREATE TRIGGER execute_steps_updated_row BEFORE UPDATE ON execute_steps FOR EACH ROW EXECUTE PROCEDURE updated_row();
CREATE INDEX ON execute_steps (execute_type_id);
INSERT INTO execute_steps (execute_type_id, command) values (1, 'gcc -lm -std=c99 __FILE__');
INSERT INTO execute_steps (execute_type_id, command) values (1, './a.out');
INSERT INTO execute_steps (execute_type_id, command) values (2, 'g++ __FILE__');
INSERT INTO execute_steps (execute_type_id, command) values (2, './a.out');
INSERT INTO execute_steps (execute_type_id, command) values (3, 'g++ -std=c++11 -O2  __FILE__');
INSERT INTO execute_steps (execute_type_id, command) values (3, './a.out');
INSERT INTO execute_steps (execute_type_id, command) values (4, 'javac __FILE__');
INSERT INTO execute_steps (execute_type_id, command) values (4, 'java -Xmx__MEMORY_LIMIT__k -Xss__MEMORY_LIMIT__k __MAIN_FILE__');
INSERT INTO execute_steps (execute_type_id, command) values (5, 'python2 -m py_compile __FILE__');
INSERT INTO execute_steps (execute_type_id, command) values (5, 'python2 __FILE__');
INSERT INTO execute_steps (execute_type_id, command) values (6, 'python3 -m py_compile __FILE__');
INSERT INTO execute_steps (execute_type_id, command) values (6, 'python3 __FILE__');

/*
CREATE TABLE verdicts(
    id              serial          NOT NULL    PRIMARY KEY,
    title           varchar(255)    ,
    execute_type_id integer         NOT NULL    DEFAULT 0   REFERENCES execute_types(id)    ON DELETE CASCADE,
    problem_id      integer         NOT NULL    DEFAULT 0,
    file_name       varchar(255)    NOT NULL,
    setter_user_id  integer         NOT NULL    REFERENCES users(id)    ON DELETE CASCADE,
    created_at      timestamp       DEFAULT date_trunc('second',now()),
    updated_at      timestamp       DEFAULT date_trunc('second',now())
);
CREATE TRIGGER verdicts_update_row BEFORE UPDATE ON verdicts FOR EACH ROW EXECUTE PROCEDURE updated_row();

CREATE TABLE score_types (
    id              serial          NOT NULL    PRIMARY KEY,
    name            varchar(255)    NOT NULL,
    created_at      timestamp       DEFAULT date_trunc('second',now()),
    updated_at      timestamp       DEFAULT date_trunc('second',now())
);
CREATE TRIGGER score_types_update_row BEFORE UPDATE ON score_types FOR EACH ROW EXECUTE PROCEDURE updated_row();
INSERT INTO score_types (name) VALUES ('sum');
INSERT INTO score_types (name) VALUES ('min');

--DROP TABLE IF EXISTS problems;
CREATE TABLE problems (
    id              serial          NOT NULL    PRIMARY KEY,
    title           varchar(255)    NOT NULL DEFAULT '',
    pdf             boolean         NOT NULL DEFAULT FALSE,
    description     text            NOT NULL DEFAULT '',
    input           text            NOT NULL DEFAULT '',
    output          text            NOT NULL DEFAULT '',
    sample_input    text            NOT NULL DEFAULT '',
    sample_output   text            NOT NULL DEFAULT '',
    hint            text            NOT NULL DEFAULT '',
    verdict_id      integer         DEFAULT 1   REFERENCES verdicts(id) ON DELETE CASCADE,
    score_type_id   integer         DEFAULT 1   REFERENCES score_types(id) ON DELETE CASCADE,
    created_at      timestamp       DEFAULT date_trunc('second',now()),
    updated_at      timestamp       DEFAULT date_trunc('second',now())
);
ALTER SEQUENCE problems_id_seq RESTART WITH 10001;
CREATE TRIGGER problems_updated_row BEFORE UPDATE ON problems FOR EACH ROW EXECUTE PROCEDURE updated_row();
CREATE INDEX ON problems (visible);
CREATE INDEX ON problems (group_id);

--DROP TABLE IF EXISTS map_problem_execute;
CREATE TABLE map_problem_execute (
    id              serial          NOT NULL    PRIMARY KEY,
    problem_id      integer         NOT NULL    REFERENCES problems(id) ON DELETE CASCADE,
    execute_type_id integer         NOT NULL    REFERENCES execute_types(id)    ON DELETE CASCADE,
    created_at      timestamp       DEFAULT date_trunc('second',now()),
    updated_at      timestamp       DEFAULT date_trunc('second',now())
);
CREATE TRIGGER map_problem_execute_updated_row BEFORE UPDATE ON map_problem_execute FOR EACH ROW EXECUTE PROCEDURE updated_row();
CREATE INDEX ON map_problem_execute (problem_id);
CREATE INDEX ON map_problem_execute (execute_type_id);
CREATE UNIQUE INDEX ON map_problem_execute (problem_id, execute_type_id);

CREATE TABLE testdata(
    id              serial          NOT NULL    PRIMARY KEY,
    problem_id      integer         NOT NULL    REFERENCES problems(id) ON DELETE CASCADE,
    time_limit      integer         NOT NULL    DEFAULT 1000,
    memory_limit    integer         NOT NULL    DEFAULT 262144,
    output_limit    integer         NOT NULL    DEFAULT 64,
    score           integer         NOT NULL    DEFAULT 0,
    created_at      timestamp       DEFAULT date_trunc('second',now()),
    updated_at      timestamp       DEFAULT date_trunc('second',now())
);
CREATE TRIGGER testdata_updated_row BEFORE UPDATE ON testdata FOR EACH ROW EXECUTE PROCEDURE updated_row();
CREATE INDEX ON testdata (problem_id);

CREATE TABLE map_verdict_string (
    id              serial          NOT NULL    PRIMARY KEY,
    abbreviation    varchar(15)     NOT NULL,
    description     varchar(31)     NOT NULL,
    priority        integer         NOT NULL,
    color           varchar(32)     NOT NULL    DEFAULT '#000',
    created_at      timestamp       DEFAULT date_trunc('second',now()),
    updated_at      timestamp       DEFAULT date_trunc('second',now())
);
CREATE TRIGGER map_verdict_string_updated_row BEFORE UPDATE ON map_verdict_string FOR EACH ROW EXECUTE PROCEDURE updated_row();
CREATE INDEX ON map_verdict_string(priority);
INSERT INTO map_verdict_string (abbreviation,description,priority,color) VALUES('Waiting', 'Waiting', 0, '#000');
INSERT INTO map_verdict_string (abbreviation,description,priority,color) VALUES('Pending', 'In Queue', 1, '#000');
INSERT INTO map_verdict_string (abbreviation,description,priority,color) VALUES('SE', 'System Error', 2, '#000');
INSERT INTO map_verdict_string (abbreviation,description,priority,color) VALUES('CE', 'Compile Error', 3, 'rgb(51, 122, 183)');
INSERT INTO map_verdict_string (abbreviation,description,priority,color) VALUES('RE', 'Runtime Error', 4, 'rgb(163, 188, 0)');
INSERT INTO map_verdict_string (abbreviation,description,priority,color) VALUES('MLE', 'Memory Limit Exceed', 5, '#000');
INSERT INTO map_verdict_string (abbreviation,description,priority,color) VALUES('TLE', 'Time Limit Exceed', 6, 'rgb(156, 39, 176)');
INSERT INTO map_verdict_string (abbreviation,description,priority,color) VALUES('OLE', 'Output Limit Exceed', 7, '#000');
INSERT INTO map_verdict_string (abbreviation,description,priority,color) VALUES('WA', 'Wrong Answer', 8, 'rgb(244, 67, 54)');
INSERT INTO map_verdict_string (abbreviation,description,priority,color) VALUES('AC', 'Accepted', 9, 'rgb(76, 175, 80)');


--DROP TABLE IF EXISTS submissions;
CREATE TABLE submissions(
    id              serial          NOT NULL    PRIMARY KEY,
    user_id         integer         NOT NULL    REFERENCES users(id)    ON DELETE CASCADE,
    problem_id      integer         NOT NULL    REFERENCES problems(id) ON DELETE CASCADE,
    execute_type_id integer         NOT NULL    REFERENCES execute_types(id)    ON DELETE CASCADE,
    time_usage      integer         ,
    memory_usage    integer         ,
    verdict         integer         NOT NULL    DEFAULT 1   REFERENCES map_verdict_string(id)   ON DELETE CASCADE,
    score           integer         ,
    length          integer         NOT NULL,
    file_name       varchar(255)    NOT NULL,
    ip              inet            NOT NULL,
    created_at      timestamp       DEFAULT date_trunc('second',now()),
    updated_at      timestamp       DEFAULT date_trunc('second',now())
);
ALTER SEQUENCE submissions_id_seq RESTART WITH 10001;
CREATE TRIGGER submissions_updated_row BEFORE UPDATE ON submissions FOR EACH ROW EXECUTE PROCEDURE updated_row();
CREATE INDEX ON submissions (user_id);
CREATE INDEX ON submissions (problem_id);
CREATE INDEX ON submissions (execute_type_id);
CREATE INDEX ON submissions (memory_usage);
CREATE INDEX ON submissions (time_usage);
CREATE INDEX ON submissions (verdict);
CREATE INDEX ON submissions (length);
CREATE INDEX ON submissions (created_at);

CREATE TABLE map_submission_testdata (
    id              serial          NOT NULL    PRIMARY KEY,
    testdata_id     integer         NOT NULL    REFERENCES testdata(id)     ON DELETE CASCADE,
    submission_id   integer         NOT NULL    REFERENCES submissions(id)  ON DELETE CASCADE,
    time_usage      integer,
    memory_usage    integer,
    score           integer,
    verdict         integer         DEFAULT 1   REFERENCES map_verdict_string(id)   ON DELETE CASCADE,
    created_at      timestamp       DEFAULT date_trunc('second',now()),
    updated_at      timestamp       DEFAULT date_trunc('second',now())
);
CREATE TRIGGER map_submission_testdata_updated_row BEFORE UPDATE ON map_submission_testdata FOR EACH ROW EXECUTE PROCEDURE updated_row();
CREATE INDEX ON map_submission_testdata(submission_id);
CREATE INDEX ON map_submission_testdata(time_usage);
CREATE INDEX ON map_submission_testdata(memory_usage);
CREATE INDEX ON map_submission_testdata(verdict);

--DROP TABLE IF EXISTS contests;
CREATE TABLE contests(
    id              serial          NOT NULL    PRIMARY KEY,
    title           varchar(255)    ,
    description     text            ,
    "start"         timestamp       NOT NULL    DEFAULT date_trunc('second', now()),
    "freeze"        integer         NOT NULL    DEFAULT 0 CHECK ("freeze" * interval '1 minute' <= "end"-"start"),
    "end"           timestamp       NOT NULL    DEFAULT date_trunc('second', now()),
    "type"          integer         NOT NULL    DEFAULT 0,
    created_at      timestamp       DEFAULT date_trunc('second',now()),
    updated_at      timestamp       DEFAULT date_trunc('second',now())
);
ALTER SEQUENCE contests_id_seq RESTART WITH 1001;
CREATE TRIGGER contests_update_row BEFORE UPDATE ON contests FOR EACH ROW EXECUTE PROCEDURE updated_row();
CREATE INDEX ON contests (group_id);
CREATE INDEX ON contests (visible);

CREATE TABLE map_contest_problem (
    problem_id      integer         NOT NULL    REFERENCES problems(id) ON DELETE CASCADE,
    penalty         integer         NOT NULL    DEFAULT 20,
    created_at      timestamp       DEFAULT date_trunc('second',now()),
    updated_at      timestamp       DEFAULT date_trunc('second',now())
);
CREATE TRIGGER map_conteset_problem_update_row BEFORE UPDATE ON map_contest_problem FOR EACH ROW EXECUTE PROCEDURE updated_row();
CREATE INDEX ON map_contest_problem (problem_id);
CREATE UNIQUE INDEX ON map_contest_problem (contest_id, problem_id);

CREATE TABLE wait_submissions (
    id              serial          NOT NULL    PRIMARY KEY,
    submission_id   integer         NOT NULL    REFERENCES submissions(id)  ON  DELETE  CASCADE,
);
CREATE TRIGGER wait_submissions_update_row BEFORE UPDATE ON wait_submissions FOR EACH ROW EXECUTE PROCEDURE updated_row();
CREATE UNIQUE INDEX ON wait_submissions(submission_id);

CREATE TABLE judge_token (
    id              serial          NOT NULL    PRIMARY KEY,
    addr            varchar(31)     DEFAULT '',
    description     varchar(255)    DEFAULT '',
    token           varchar(255)    NOT NULL,
    created_at      timestamp       DEFAULT date_trunc('second',now()),
    updated_at      timestamp       DEFAULT date_trunc('second',now())
);
CREATE TRIGGER judge_token_update_row BEFORE UPDATE ON judge_token FOR EACH ROW EXECUTE PROCEDURE updated_row();
CREATE UNIQUE INDEX ON judge_token(token);
INSERT INTO judge_token (token) VALUES('TOKEN');
*/