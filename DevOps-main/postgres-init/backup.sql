CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);

CREATE TABLE public.goals (
    id integer NOT NULL,
    sem integer NOT NULL,
    student integer NOT NULL,
    disc_name integer NOT NULL,
    goal character varying(10) NOT NULL
);

CREATE SEQUENCE public.goals_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER SEQUENCE public.goals_id_seq OWNED BY public.goals.id;

ALTER TABLE ONLY public.goals ALTER COLUMN id SET DEFAULT nextval('public.goals_id_seq'::regclass);

CREATE TABLE public.plan (
    id integer NOT NULL,
    spec_name character varying(200) NOT NULL,
    disc_name character varying(200) NOT NULL,
    sem integer NOT NULL,
    amount integer NOT NULL,
    exam boolean NOT NULL
);

CREATE SEQUENCE public.plan_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER SEQUENCE public.plan_id_seq OWNED BY public.plan.id;

ALTER TABLE ONLY public.plan ALTER COLUMN id SET DEFAULT nextval('public.plan_id_seq'::regclass);

CREATE TABLE public.roles (
    id integer NOT NULL,
    role_name character varying(50) NOT NULL,
    description character varying(100)
);

CREATE SEQUENCE public.roles_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER SEQUENCE public.roles_id_seq OWNED BY public.roles.id;

ALTER TABLE ONLY public.roles ALTER COLUMN id SET DEFAULT nextval('public.roles_id_seq'::regclass);

CREATE TABLE public.users (
    id integer NOT NULL,
    login character varying(50) NOT NULL,
    password_hash character varying(200) NOT NULL,
    last_name character varying(50) NOT NULL,
    first_name character varying(50) NOT NULL,
    middle_name character varying(50),
    form character varying(50) NOT NULL,
    date integer NOT NULL,
    "group" character varying(50),
    role_id integer NOT NULL
);

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);

ALTER TABLE ONLY public.goals ADD CONSTRAINT pk_goals PRIMARY KEY (id);

ALTER TABLE ONLY public.plan ADD CONSTRAINT pk_plan PRIMARY KEY (id);

ALTER TABLE ONLY public.roles ADD CONSTRAINT pk_roles PRIMARY KEY (id);

ALTER TABLE ONLY public.users ADD CONSTRAINT pk_users PRIMARY KEY (id);

ALTER TABLE ONLY public.roles ADD CONSTRAINT uq_roles_role_name UNIQUE (role_name);

ALTER TABLE ONLY public.users ADD CONSTRAINT uq_users_login UNIQUE (login);

ALTER TABLE ONLY public.users
    ADD CONSTRAINT fk_users_role_id_roles FOREIGN KEY (role_id) REFERENCES public.roles(id) ON DELETE CASCADE;

INSERT INTO public.alembic_version (version_num) VALUES ('628a9b3bfa2c');

INSERT INTO public.roles (id, role_name, description) VALUES (1, 'Admin', 'Administrator role');
INSERT INTO public.roles (id, role_name, description) VALUES (2, 'Moderator', 'Moderator role');
INSERT INTO public.roles (id, role_name, description) VALUES (3, 'admin', 'Administrator');
INSERT INTO public.roles (id, role_name, description) VALUES (4, 'moder', 'Moderator');
INSERT INTO public.roles (id, role_name, description) VALUES (9, 'AAdmin', 'Administrator');
INSERT INTO public.roles (id, role_name, description) VALUES (10, 'mmoder', 'Moderator');

INSERT INTO public.users (id, login, password_hash, last_name, first_name, middle_name, form, date, "group", role_id) VALUES (1, 'admin', 'scrypt:32768:8:1$rRIWKEpYpMnrwBYx$a4e2de48892da0e017b32fa79dd543453e5122146c12bd6d82d0b2e58902c0634e28dd387ff76c5b1bc4f8f1b9a29b86410a668630a743558254a181afda581a', 'Admin', 'User', 'Test', 'Дневная', 2024, 'A', 1);
