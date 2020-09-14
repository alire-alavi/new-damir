--
-- PostgreSQL database dump
--

-- Dumped from database version 12.4 (Ubuntu 12.4-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.4 (Ubuntu 12.4-0ubuntu0.20.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: account_emailaddress; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.account_emailaddress (
    id integer NOT NULL,
    email character varying(254) NOT NULL,
    verified boolean NOT NULL,
    "primary" boolean NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.account_emailaddress OWNER TO jeremih;

--
-- Name: account_emailaddress_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.account_emailaddress_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.account_emailaddress_id_seq OWNER TO jeremih;

--
-- Name: account_emailaddress_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.account_emailaddress_id_seq OWNED BY public.account_emailaddress.id;


--
-- Name: account_emailconfirmation; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.account_emailconfirmation (
    id integer NOT NULL,
    created timestamp with time zone NOT NULL,
    sent timestamp with time zone,
    key character varying(64) NOT NULL,
    email_address_id integer NOT NULL
);


ALTER TABLE public.account_emailconfirmation OWNER TO jeremih;

--
-- Name: account_emailconfirmation_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.account_emailconfirmation_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.account_emailconfirmation_id_seq OWNER TO jeremih;

--
-- Name: account_emailconfirmation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.account_emailconfirmation_id_seq OWNED BY public.account_emailconfirmation.id;


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO jeremih;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO jeremih;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO jeremih;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO jeremih;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO jeremih;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO jeremih;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: authtoken_token; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.authtoken_token (
    key character varying(40) NOT NULL,
    created timestamp with time zone NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.authtoken_token OWNER TO jeremih;

--
-- Name: blog_comment; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.blog_comment (
    id integer NOT NULL,
    "timestamp" timestamp with time zone NOT NULL,
    content text NOT NULL,
    post_id integer NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.blog_comment OWNER TO jeremih;

--
-- Name: blog_comment_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.blog_comment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.blog_comment_id_seq OWNER TO jeremih;

--
-- Name: blog_comment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.blog_comment_id_seq OWNED BY public.blog_comment.id;


--
-- Name: blog_post; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.blog_post (
    id integer NOT NULL,
    title character varying(1024) NOT NULL,
    short_description text NOT NULL,
    content text NOT NULL,
    "timestamp" date NOT NULL,
    thumbnail character varying(100) NOT NULL,
    featured boolean NOT NULL,
    active_post boolean NOT NULL,
    slug character varying(50),
    author_id integer NOT NULL
);


ALTER TABLE public.blog_post OWNER TO jeremih;

--
-- Name: blog_post_categories; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.blog_post_categories (
    id integer NOT NULL,
    post_id integer NOT NULL,
    category_id integer NOT NULL
);


ALTER TABLE public.blog_post_categories OWNER TO jeremih;

--
-- Name: blog_post_categories_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.blog_post_categories_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.blog_post_categories_id_seq OWNER TO jeremih;

--
-- Name: blog_post_categories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.blog_post_categories_id_seq OWNED BY public.blog_post_categories.id;


--
-- Name: blog_post_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.blog_post_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.blog_post_id_seq OWNER TO jeremih;

--
-- Name: blog_post_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.blog_post_id_seq OWNED BY public.blog_post.id;


--
-- Name: categories_category; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.categories_category (
    id integer NOT NULL,
    title character varying(64) NOT NULL,
    sub_category_of_id integer NOT NULL
);


ALTER TABLE public.categories_category OWNER TO jeremih;

--
-- Name: categories_category_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.categories_category_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.categories_category_id_seq OWNER TO jeremih;

--
-- Name: categories_category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.categories_category_id_seq OWNED BY public.categories_category.id;


--
-- Name: categories_categoryvariation; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.categories_categoryvariation (
    id integer NOT NULL,
    value character varying(50),
    attachment character varying(100),
    selectable boolean,
    yes_or_no boolean,
    variation_id integer NOT NULL
);


ALTER TABLE public.categories_categoryvariation OWNER TO jeremih;

--
-- Name: categories_categoryvariation_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.categories_categoryvariation_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.categories_categoryvariation_id_seq OWNER TO jeremih;

--
-- Name: categories_categoryvariation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.categories_categoryvariation_id_seq OWNED BY public.categories_categoryvariation.id;


--
-- Name: categories_maincategory; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.categories_maincategory (
    id integer NOT NULL,
    title character varying(64) NOT NULL
);


ALTER TABLE public.categories_maincategory OWNER TO jeremih;

--
-- Name: categories_maincategory_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.categories_maincategory_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.categories_maincategory_id_seq OWNER TO jeremih;

--
-- Name: categories_maincategory_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.categories_maincategory_id_seq OWNED BY public.categories_maincategory.id;


--
-- Name: categories_variation; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.categories_variation (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    category_id integer NOT NULL
);


ALTER TABLE public.categories_variation OWNER TO jeremih;

--
-- Name: categories_variation_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.categories_variation_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.categories_variation_id_seq OWNER TO jeremih;

--
-- Name: categories_variation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.categories_variation_id_seq OWNED BY public.categories_variation.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO jeremih;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO jeremih;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO jeremih;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO jeremih;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO jeremih;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO jeremih;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO jeremih;

--
-- Name: django_site; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.django_site (
    id integer NOT NULL,
    domain character varying(100) NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.django_site OWNER TO jeremih;

--
-- Name: django_site_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.django_site_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_site_id_seq OWNER TO jeremih;

--
-- Name: django_site_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.django_site_id_seq OWNED BY public.django_site.id;


--
-- Name: hitcount_blacklist_ip; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.hitcount_blacklist_ip (
    id integer NOT NULL,
    ip character varying(40) NOT NULL
);


ALTER TABLE public.hitcount_blacklist_ip OWNER TO jeremih;

--
-- Name: hitcount_blacklist_ip_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.hitcount_blacklist_ip_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.hitcount_blacklist_ip_id_seq OWNER TO jeremih;

--
-- Name: hitcount_blacklist_ip_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.hitcount_blacklist_ip_id_seq OWNED BY public.hitcount_blacklist_ip.id;


--
-- Name: hitcount_blacklist_user_agent; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.hitcount_blacklist_user_agent (
    id integer NOT NULL,
    user_agent character varying(255) NOT NULL
);


ALTER TABLE public.hitcount_blacklist_user_agent OWNER TO jeremih;

--
-- Name: hitcount_blacklist_user_agent_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.hitcount_blacklist_user_agent_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.hitcount_blacklist_user_agent_id_seq OWNER TO jeremih;

--
-- Name: hitcount_blacklist_user_agent_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.hitcount_blacklist_user_agent_id_seq OWNED BY public.hitcount_blacklist_user_agent.id;


--
-- Name: hitcount_hit; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.hitcount_hit (
    id integer NOT NULL,
    created timestamp with time zone NOT NULL,
    ip character varying(40) NOT NULL,
    session character varying(40) NOT NULL,
    user_agent character varying(255) NOT NULL,
    hitcount_id integer NOT NULL,
    user_id integer
);


ALTER TABLE public.hitcount_hit OWNER TO jeremih;

--
-- Name: hitcount_hit_count; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.hitcount_hit_count (
    id integer NOT NULL,
    hits integer NOT NULL,
    modified timestamp with time zone NOT NULL,
    object_pk integer NOT NULL,
    content_type_id integer NOT NULL,
    CONSTRAINT hitcount_hit_count_hits_check CHECK ((hits >= 0)),
    CONSTRAINT hitcount_hit_count_object_pk_53e9c38f_check CHECK ((object_pk >= 0))
);


ALTER TABLE public.hitcount_hit_count OWNER TO jeremih;

--
-- Name: hitcount_hit_count_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.hitcount_hit_count_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.hitcount_hit_count_id_seq OWNER TO jeremih;

--
-- Name: hitcount_hit_count_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.hitcount_hit_count_id_seq OWNED BY public.hitcount_hit_count.id;


--
-- Name: hitcount_hit_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.hitcount_hit_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.hitcount_hit_id_seq OWNER TO jeremih;

--
-- Name: hitcount_hit_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.hitcount_hit_id_seq OWNED BY public.hitcount_hit.id;


--
-- Name: merchandise_address; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.merchandise_address (
    id integer NOT NULL,
    street_address character varying(100) NOT NULL,
    apartment_address character varying(100) NOT NULL,
    zip character varying(100) NOT NULL,
    address_type character varying(1) NOT NULL,
    "default" boolean NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.merchandise_address OWNER TO jeremih;

--
-- Name: merchandise_address_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.merchandise_address_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.merchandise_address_id_seq OWNER TO jeremih;

--
-- Name: merchandise_address_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.merchandise_address_id_seq OWNED BY public.merchandise_address.id;


--
-- Name: merchandise_coupon; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.merchandise_coupon (
    id integer NOT NULL,
    code character varying(15) NOT NULL,
    amount double precision NOT NULL
);


ALTER TABLE public.merchandise_coupon OWNER TO jeremih;

--
-- Name: merchandise_coupon_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.merchandise_coupon_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.merchandise_coupon_id_seq OWNER TO jeremih;

--
-- Name: merchandise_coupon_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.merchandise_coupon_id_seq OWNED BY public.merchandise_coupon.id;


--
-- Name: merchandise_order; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.merchandise_order (
    id integer NOT NULL,
    ref_code character varying(20),
    start_date timestamp with time zone NOT NULL,
    ordered_date timestamp with time zone NOT NULL,
    ordered boolean NOT NULL,
    being_delivered boolean NOT NULL,
    received boolean NOT NULL,
    refund_requested boolean NOT NULL,
    refund_granted boolean NOT NULL,
    billing_address_id integer,
    coupon_id integer,
    payment_id integer,
    shipping_address_id integer,
    user_id integer NOT NULL
);


ALTER TABLE public.merchandise_order OWNER TO jeremih;

--
-- Name: merchandise_order_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.merchandise_order_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.merchandise_order_id_seq OWNER TO jeremih;

--
-- Name: merchandise_order_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.merchandise_order_id_seq OWNED BY public.merchandise_order.id;


--
-- Name: merchandise_order_items; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.merchandise_order_items (
    id integer NOT NULL,
    order_id integer NOT NULL,
    orderitem_id integer NOT NULL
);


ALTER TABLE public.merchandise_order_items OWNER TO jeremih;

--
-- Name: merchandise_order_items_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.merchandise_order_items_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.merchandise_order_items_id_seq OWNER TO jeremih;

--
-- Name: merchandise_order_items_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.merchandise_order_items_id_seq OWNED BY public.merchandise_order_items.id;


--
-- Name: merchandise_order_producer; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.merchandise_order_producer (
    id integer NOT NULL,
    order_id integer NOT NULL,
    producerprofile_id integer NOT NULL
);


ALTER TABLE public.merchandise_order_producer OWNER TO jeremih;

--
-- Name: merchandise_order_producer_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.merchandise_order_producer_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.merchandise_order_producer_id_seq OWNER TO jeremih;

--
-- Name: merchandise_order_producer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.merchandise_order_producer_id_seq OWNED BY public.merchandise_order_producer.id;


--
-- Name: merchandise_orderitem; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.merchandise_orderitem (
    id integer NOT NULL,
    ordered boolean NOT NULL,
    quantity integer NOT NULL,
    item_id integer NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.merchandise_orderitem OWNER TO jeremih;

--
-- Name: merchandise_orderitem_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.merchandise_orderitem_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.merchandise_orderitem_id_seq OWNER TO jeremih;

--
-- Name: merchandise_orderitem_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.merchandise_orderitem_id_seq OWNED BY public.merchandise_orderitem.id;


--
-- Name: merchandise_payment; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.merchandise_payment (
    id integer NOT NULL,
    stripe_charge_id character varying(50) NOT NULL,
    amount double precision NOT NULL,
    "timestamp" timestamp with time zone NOT NULL,
    user_id integer
);


ALTER TABLE public.merchandise_payment OWNER TO jeremih;

--
-- Name: merchandise_payment_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.merchandise_payment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.merchandise_payment_id_seq OWNER TO jeremih;

--
-- Name: merchandise_payment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.merchandise_payment_id_seq OWNED BY public.merchandise_payment.id;


--
-- Name: merchandise_refund; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.merchandise_refund (
    id integer NOT NULL,
    reason text NOT NULL,
    accepted boolean NOT NULL,
    email character varying(254) NOT NULL,
    order_id integer NOT NULL
);


ALTER TABLE public.merchandise_refund OWNER TO jeremih;

--
-- Name: merchandise_refund_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.merchandise_refund_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.merchandise_refund_id_seq OWNER TO jeremih;

--
-- Name: merchandise_refund_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.merchandise_refund_id_seq OWNED BY public.merchandise_refund.id;


--
-- Name: pages_document; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.pages_document (
    id integer NOT NULL,
    name character varying(10240132),
    document character varying(100) NOT NULL,
    uploaded_at timestamp with time zone NOT NULL
);


ALTER TABLE public.pages_document OWNER TO jeremih;

--
-- Name: pages_document_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.pages_document_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pages_document_id_seq OWNER TO jeremih;

--
-- Name: pages_document_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.pages_document_id_seq OWNED BY public.pages_document.id;


--
-- Name: pages_newstelleremails; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.pages_newstelleremails (
    id integer NOT NULL,
    email character varying(254) NOT NULL,
    user_id integer
);


ALTER TABLE public.pages_newstelleremails OWNER TO jeremih;

--
-- Name: pages_newstelleremails_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.pages_newstelleremails_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pages_newstelleremails_id_seq OWNER TO jeremih;

--
-- Name: pages_newstelleremails_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.pages_newstelleremails_id_seq OWNED BY public.pages_newstelleremails.id;


--
-- Name: products_product; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.products_product (
    id integer NOT NULL,
    title character varying(132) NOT NULL,
    price double precision,
    discount_price double precision,
    product_image character varying(100),
    slug character varying(50),
    stock integer NOT NULL,
    description text NOT NULL,
    minimum_order character varying(32),
    payment_type character varying(32),
    packing character varying(32),
    shipping character varying(32),
    origin character varying(32),
    made_in character varying(32),
    delivery character varying(32),
    samples character varying(24),
    remarks text,
    producer_id integer NOT NULL
);


ALTER TABLE public.products_product OWNER TO jeremih;

--
-- Name: products_product_category; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.products_product_category (
    id integer NOT NULL,
    product_id integer NOT NULL,
    category_id integer NOT NULL
);


ALTER TABLE public.products_product_category OWNER TO jeremih;

--
-- Name: products_product_category_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.products_product_category_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.products_product_category_id_seq OWNER TO jeremih;

--
-- Name: products_product_category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.products_product_category_id_seq OWNED BY public.products_product_category.id;


--
-- Name: products_product_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.products_product_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.products_product_id_seq OWNER TO jeremih;

--
-- Name: products_product_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.products_product_id_seq OWNED BY public.products_product.id;


--
-- Name: products_productcomment; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.products_productcomment (
    id integer NOT NULL,
    is_confirmed boolean NOT NULL,
    content text NOT NULL,
    product_id integer NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.products_productcomment OWNER TO jeremih;

--
-- Name: products_productcomment_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.products_productcomment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.products_productcomment_id_seq OWNER TO jeremih;

--
-- Name: products_productcomment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.products_productcomment_id_seq OWNED BY public.products_productcomment.id;


--
-- Name: products_productvariation; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.products_productvariation (
    id integer NOT NULL,
    value character varying(50) NOT NULL,
    attachment character varying(100) NOT NULL,
    variation_id integer NOT NULL
);


ALTER TABLE public.products_productvariation OWNER TO jeremih;

--
-- Name: products_productvariation_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.products_productvariation_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.products_productvariation_id_seq OWNER TO jeremih;

--
-- Name: products_productvariation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.products_productvariation_id_seq OWNED BY public.products_productvariation.id;


--
-- Name: products_rating; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.products_rating (
    id integer NOT NULL,
    stars integer NOT NULL,
    product_id integer NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.products_rating OWNER TO jeremih;

--
-- Name: products_rating_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.products_rating_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.products_rating_id_seq OWNER TO jeremih;

--
-- Name: products_rating_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.products_rating_id_seq OWNED BY public.products_rating.id;


--
-- Name: products_variation; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.products_variation (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    product_id integer NOT NULL
);


ALTER TABLE public.products_variation OWNER TO jeremih;

--
-- Name: products_variation_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.products_variation_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.products_variation_id_seq OWNER TO jeremih;

--
-- Name: products_variation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.products_variation_id_seq OWNED BY public.products_variation.id;


--
-- Name: socialaccount_socialaccount; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.socialaccount_socialaccount (
    id integer NOT NULL,
    provider character varying(30) NOT NULL,
    uid character varying(191) NOT NULL,
    last_login timestamp with time zone NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    extra_data text NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.socialaccount_socialaccount OWNER TO jeremih;

--
-- Name: socialaccount_socialaccount_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.socialaccount_socialaccount_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.socialaccount_socialaccount_id_seq OWNER TO jeremih;

--
-- Name: socialaccount_socialaccount_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.socialaccount_socialaccount_id_seq OWNED BY public.socialaccount_socialaccount.id;


--
-- Name: socialaccount_socialapp; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.socialaccount_socialapp (
    id integer NOT NULL,
    provider character varying(30) NOT NULL,
    name character varying(40) NOT NULL,
    client_id character varying(191) NOT NULL,
    secret character varying(191) NOT NULL,
    key character varying(191) NOT NULL
);


ALTER TABLE public.socialaccount_socialapp OWNER TO jeremih;

--
-- Name: socialaccount_socialapp_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.socialaccount_socialapp_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.socialaccount_socialapp_id_seq OWNER TO jeremih;

--
-- Name: socialaccount_socialapp_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.socialaccount_socialapp_id_seq OWNED BY public.socialaccount_socialapp.id;


--
-- Name: socialaccount_socialapp_sites; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.socialaccount_socialapp_sites (
    id integer NOT NULL,
    socialapp_id integer NOT NULL,
    site_id integer NOT NULL
);


ALTER TABLE public.socialaccount_socialapp_sites OWNER TO jeremih;

--
-- Name: socialaccount_socialapp_sites_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.socialaccount_socialapp_sites_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.socialaccount_socialapp_sites_id_seq OWNER TO jeremih;

--
-- Name: socialaccount_socialapp_sites_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.socialaccount_socialapp_sites_id_seq OWNED BY public.socialaccount_socialapp_sites.id;


--
-- Name: socialaccount_socialtoken; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.socialaccount_socialtoken (
    id integer NOT NULL,
    token text NOT NULL,
    token_secret text NOT NULL,
    expires_at timestamp with time zone,
    account_id integer NOT NULL,
    app_id integer NOT NULL
);


ALTER TABLE public.socialaccount_socialtoken OWNER TO jeremih;

--
-- Name: socialaccount_socialtoken_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.socialaccount_socialtoken_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.socialaccount_socialtoken_id_seq OWNER TO jeremih;

--
-- Name: socialaccount_socialtoken_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.socialaccount_socialtoken_id_seq OWNED BY public.socialaccount_socialtoken.id;


--
-- Name: users_producerprofile; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.users_producerprofile (
    profile_ptr_id integer NOT NULL,
    department character varying(132),
    job_title character varying(132),
    postal_code character varying(12),
    alternative_phone character varying(15),
    fax_number character varying(20),
    business_type character varying(20)
);


ALTER TABLE public.users_producerprofile OWNER TO jeremih;

--
-- Name: users_producerprofile_categoty; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.users_producerprofile_categoty (
    id integer NOT NULL,
    producerprofile_id integer NOT NULL,
    category_id integer NOT NULL
);


ALTER TABLE public.users_producerprofile_categoty OWNER TO jeremih;

--
-- Name: users_producerprofile_categoty_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.users_producerprofile_categoty_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_producerprofile_categoty_id_seq OWNER TO jeremih;

--
-- Name: users_producerprofile_categoty_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.users_producerprofile_categoty_id_seq OWNED BY public.users_producerprofile_categoty.id;


--
-- Name: users_profile; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.users_profile (
    id integer NOT NULL,
    gender character varying(17) NOT NULL,
    profile_picture character varying(100),
    province character varying(132),
    city character varying(132),
    company_name character varying(132),
    phone_number character varying(20),
    company_address text,
    office_address text,
    office_phone_num character varying(20),
    introduce_yourself text,
    description text,
    date_created_at timestamp with time zone NOT NULL,
    web_site character varying(120),
    user_id integer NOT NULL
);


ALTER TABLE public.users_profile OWNER TO jeremih;

--
-- Name: users_profile_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.users_profile_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_profile_id_seq OWNER TO jeremih;

--
-- Name: users_profile_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.users_profile_id_seq OWNED BY public.users_profile.id;


--
-- Name: users_user; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.users_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    is_producer boolean,
    role character varying(12)
);


ALTER TABLE public.users_user OWNER TO jeremih;

--
-- Name: users_user_groups; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.users_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.users_user_groups OWNER TO jeremih;

--
-- Name: users_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.users_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_user_groups_id_seq OWNER TO jeremih;

--
-- Name: users_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.users_user_groups_id_seq OWNED BY public.users_user_groups.id;


--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_user_id_seq OWNER TO jeremih;

--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users_user.id;


--
-- Name: users_user_user_permissions; Type: TABLE; Schema: public; Owner: jeremih
--

CREATE TABLE public.users_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.users_user_user_permissions OWNER TO jeremih;

--
-- Name: users_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: jeremih
--

CREATE SEQUENCE public.users_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_user_user_permissions_id_seq OWNER TO jeremih;

--
-- Name: users_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jeremih
--

ALTER SEQUENCE public.users_user_user_permissions_id_seq OWNED BY public.users_user_user_permissions.id;


--
-- Name: account_emailaddress id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.account_emailaddress ALTER COLUMN id SET DEFAULT nextval('public.account_emailaddress_id_seq'::regclass);


--
-- Name: account_emailconfirmation id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.account_emailconfirmation ALTER COLUMN id SET DEFAULT nextval('public.account_emailconfirmation_id_seq'::regclass);


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: blog_comment id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.blog_comment ALTER COLUMN id SET DEFAULT nextval('public.blog_comment_id_seq'::regclass);


--
-- Name: blog_post id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.blog_post ALTER COLUMN id SET DEFAULT nextval('public.blog_post_id_seq'::regclass);


--
-- Name: blog_post_categories id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.blog_post_categories ALTER COLUMN id SET DEFAULT nextval('public.blog_post_categories_id_seq'::regclass);


--
-- Name: categories_category id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.categories_category ALTER COLUMN id SET DEFAULT nextval('public.categories_category_id_seq'::regclass);


--
-- Name: categories_categoryvariation id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.categories_categoryvariation ALTER COLUMN id SET DEFAULT nextval('public.categories_categoryvariation_id_seq'::regclass);


--
-- Name: categories_maincategory id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.categories_maincategory ALTER COLUMN id SET DEFAULT nextval('public.categories_maincategory_id_seq'::regclass);


--
-- Name: categories_variation id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.categories_variation ALTER COLUMN id SET DEFAULT nextval('public.categories_variation_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: django_site id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.django_site ALTER COLUMN id SET DEFAULT nextval('public.django_site_id_seq'::regclass);


--
-- Name: hitcount_blacklist_ip id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.hitcount_blacklist_ip ALTER COLUMN id SET DEFAULT nextval('public.hitcount_blacklist_ip_id_seq'::regclass);


--
-- Name: hitcount_blacklist_user_agent id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.hitcount_blacklist_user_agent ALTER COLUMN id SET DEFAULT nextval('public.hitcount_blacklist_user_agent_id_seq'::regclass);


--
-- Name: hitcount_hit id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.hitcount_hit ALTER COLUMN id SET DEFAULT nextval('public.hitcount_hit_id_seq'::regclass);


--
-- Name: hitcount_hit_count id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.hitcount_hit_count ALTER COLUMN id SET DEFAULT nextval('public.hitcount_hit_count_id_seq'::regclass);


--
-- Name: merchandise_address id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.merchandise_address ALTER COLUMN id SET DEFAULT nextval('public.merchandise_address_id_seq'::regclass);


--
-- Name: merchandise_coupon id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.merchandise_coupon ALTER COLUMN id SET DEFAULT nextval('public.merchandise_coupon_id_seq'::regclass);


--
-- Name: merchandise_order id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.merchandise_order ALTER COLUMN id SET DEFAULT nextval('public.merchandise_order_id_seq'::regclass);


--
-- Name: merchandise_order_items id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.merchandise_order_items ALTER COLUMN id SET DEFAULT nextval('public.merchandise_order_items_id_seq'::regclass);


--
-- Name: merchandise_order_producer id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.merchandise_order_producer ALTER COLUMN id SET DEFAULT nextval('public.merchandise_order_producer_id_seq'::regclass);


--
-- Name: merchandise_orderitem id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.merchandise_orderitem ALTER COLUMN id SET DEFAULT nextval('public.merchandise_orderitem_id_seq'::regclass);


--
-- Name: merchandise_payment id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.merchandise_payment ALTER COLUMN id SET DEFAULT nextval('public.merchandise_payment_id_seq'::regclass);


--
-- Name: merchandise_refund id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.merchandise_refund ALTER COLUMN id SET DEFAULT nextval('public.merchandise_refund_id_seq'::regclass);


--
-- Name: pages_document id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.pages_document ALTER COLUMN id SET DEFAULT nextval('public.pages_document_id_seq'::regclass);


--
-- Name: pages_newstelleremails id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.pages_newstelleremails ALTER COLUMN id SET DEFAULT nextval('public.pages_newstelleremails_id_seq'::regclass);


--
-- Name: products_product id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.products_product ALTER COLUMN id SET DEFAULT nextval('public.products_product_id_seq'::regclass);


--
-- Name: products_product_category id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.products_product_category ALTER COLUMN id SET DEFAULT nextval('public.products_product_category_id_seq'::regclass);


--
-- Name: products_productcomment id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.products_productcomment ALTER COLUMN id SET DEFAULT nextval('public.products_productcomment_id_seq'::regclass);


--
-- Name: products_productvariation id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.products_productvariation ALTER COLUMN id SET DEFAULT nextval('public.products_productvariation_id_seq'::regclass);


--
-- Name: products_rating id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.products_rating ALTER COLUMN id SET DEFAULT nextval('public.products_rating_id_seq'::regclass);


--
-- Name: products_variation id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.products_variation ALTER COLUMN id SET DEFAULT nextval('public.products_variation_id_seq'::regclass);


--
-- Name: socialaccount_socialaccount id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.socialaccount_socialaccount ALTER COLUMN id SET DEFAULT nextval('public.socialaccount_socialaccount_id_seq'::regclass);


--
-- Name: socialaccount_socialapp id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.socialaccount_socialapp ALTER COLUMN id SET DEFAULT nextval('public.socialaccount_socialapp_id_seq'::regclass);


--
-- Name: socialaccount_socialapp_sites id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.socialaccount_socialapp_sites ALTER COLUMN id SET DEFAULT nextval('public.socialaccount_socialapp_sites_id_seq'::regclass);


--
-- Name: socialaccount_socialtoken id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.socialaccount_socialtoken ALTER COLUMN id SET DEFAULT nextval('public.socialaccount_socialtoken_id_seq'::regclass);


--
-- Name: users_producerprofile_categoty id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.users_producerprofile_categoty ALTER COLUMN id SET DEFAULT nextval('public.users_producerprofile_categoty_id_seq'::regclass);


--
-- Name: users_profile id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.users_profile ALTER COLUMN id SET DEFAULT nextval('public.users_profile_id_seq'::regclass);


--
-- Name: users_user id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.users_user ALTER COLUMN id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- Name: users_user_groups id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.users_user_groups ALTER COLUMN id SET DEFAULT nextval('public.users_user_groups_id_seq'::regclass);


--
-- Name: users_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.users_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.users_user_user_permissions_id_seq'::regclass);


--
-- Data for Name: account_emailaddress; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.account_emailaddress (id, email, verified, "primary", user_id) FROM stdin;
1	alire@yahoo.com	f	f	2
2	aeaef@track.com	f	f	3
\.


--
-- Data for Name: account_emailconfirmation; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.account_emailconfirmation (id, created, sent, key, email_address_id) FROM stdin;
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add permission	1	add_permission
2	Can change permission	1	change_permission
3	Can delete permission	1	delete_permission
4	Can view permission	1	view_permission
5	Can add group	2	add_group
6	Can change group	2	change_group
7	Can delete group	2	delete_group
8	Can view group	2	view_group
9	Can add content type	3	add_contenttype
10	Can change content type	3	change_contenttype
11	Can delete content type	3	delete_contenttype
12	Can view content type	3	view_contenttype
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add profile	5	add_profile
18	Can change profile	5	change_profile
19	Can delete profile	5	delete_profile
20	Can view profile	5	view_profile
21	Can add producer profile	6	add_producerprofile
22	Can change producer profile	6	change_producerprofile
23	Can delete producer profile	6	delete_producerprofile
24	Can view producer profile	6	view_producerprofile
25	Can add category	7	add_category
26	Can change category	7	change_category
27	Can delete category	7	delete_category
28	Can view category	7	view_category
29	Can add main category	8	add_maincategory
30	Can change main category	8	change_maincategory
31	Can delete main category	8	delete_maincategory
32	Can view main category	8	view_maincategory
33	Can add variation	9	add_variation
34	Can change variation	9	change_variation
35	Can delete variation	9	delete_variation
36	Can view variation	9	view_variation
37	Can add category variation	10	add_categoryvariation
38	Can change category variation	10	change_categoryvariation
39	Can delete category variation	10	delete_categoryvariation
40	Can view category variation	10	view_categoryvariation
41	Can add comment	11	add_comment
42	Can change comment	11	change_comment
43	Can delete comment	11	delete_comment
44	Can view comment	11	view_comment
45	Can add post	12	add_post
46	Can change post	12	change_post
47	Can delete post	12	delete_post
48	Can view post	12	view_post
49	Can add order item	13	add_orderitem
50	Can change order item	13	change_orderitem
51	Can delete order item	13	delete_orderitem
52	Can view order item	13	view_orderitem
53	Can add order	14	add_order
54	Can change order	14	change_order
55	Can delete order	14	delete_order
56	Can view order	14	view_order
57	Can add address	15	add_address
58	Can change address	15	change_address
59	Can delete address	15	delete_address
60	Can view address	15	view_address
61	Can add payment	16	add_payment
62	Can change payment	16	change_payment
63	Can delete payment	16	delete_payment
64	Can view payment	16	view_payment
65	Can add coupon	17	add_coupon
66	Can change coupon	17	change_coupon
67	Can delete coupon	17	delete_coupon
68	Can view coupon	17	view_coupon
69	Can add refund	18	add_refund
70	Can change refund	18	change_refund
71	Can delete refund	18	delete_refund
72	Can view refund	18	view_refund
73	Can add product	19	add_product
74	Can change product	19	change_product
75	Can delete product	19	delete_product
76	Can view product	19	view_product
77	Can add variation	20	add_variation
78	Can change variation	20	change_variation
79	Can delete variation	20	delete_variation
80	Can view variation	20	view_variation
81	Can add product variation	21	add_productvariation
82	Can change product variation	21	change_productvariation
83	Can delete product variation	21	delete_productvariation
84	Can view product variation	21	view_productvariation
85	Can add product comment	22	add_productcomment
86	Can change product comment	22	change_productcomment
87	Can delete product comment	22	delete_productcomment
88	Can view product comment	22	view_productcomment
89	Can add rating	23	add_rating
90	Can change rating	23	change_rating
91	Can delete rating	23	delete_rating
92	Can view rating	23	view_rating
93	Can add news teller emails	24	add_newstelleremails
94	Can change news teller emails	24	change_newstelleremails
95	Can delete news teller emails	24	delete_newstelleremails
96	Can view news teller emails	24	view_newstelleremails
97	Can add document	25	add_document
98	Can change document	25	change_document
99	Can delete document	25	delete_document
100	Can view document	25	view_document
101	Can add log entry	26	add_logentry
102	Can change log entry	26	change_logentry
103	Can delete log entry	26	delete_logentry
104	Can view log entry	26	view_logentry
105	Can add session	27	add_session
106	Can change session	27	change_session
107	Can delete session	27	delete_session
108	Can view session	27	view_session
109	Can add site	28	add_site
110	Can change site	28	change_site
111	Can delete site	28	delete_site
112	Can view site	28	view_site
113	Can add Token	29	add_token
114	Can change Token	29	change_token
115	Can delete Token	29	delete_token
116	Can view Token	29	view_token
117	Can add email address	30	add_emailaddress
118	Can change email address	30	change_emailaddress
119	Can delete email address	30	delete_emailaddress
120	Can view email address	30	view_emailaddress
121	Can add email confirmation	31	add_emailconfirmation
122	Can change email confirmation	31	change_emailconfirmation
123	Can delete email confirmation	31	delete_emailconfirmation
124	Can view email confirmation	31	view_emailconfirmation
125	Can add social account	32	add_socialaccount
126	Can change social account	32	change_socialaccount
127	Can delete social account	32	delete_socialaccount
128	Can view social account	32	view_socialaccount
129	Can add social application	33	add_socialapp
130	Can change social application	33	change_socialapp
131	Can delete social application	33	delete_socialapp
132	Can view social application	33	view_socialapp
133	Can add social application token	34	add_socialtoken
134	Can change social application token	34	change_socialtoken
135	Can delete social application token	34	delete_socialtoken
136	Can view social application token	34	view_socialtoken
137	Can add Blacklisted IP	35	add_blacklistip
138	Can change Blacklisted IP	35	change_blacklistip
139	Can delete Blacklisted IP	35	delete_blacklistip
140	Can view Blacklisted IP	35	view_blacklistip
141	Can add Blacklisted User Agent	36	add_blacklistuseragent
142	Can change Blacklisted User Agent	36	change_blacklistuseragent
143	Can delete Blacklisted User Agent	36	delete_blacklistuseragent
144	Can view Blacklisted User Agent	36	view_blacklistuseragent
145	Can add hit	37	add_hit
146	Can change hit	37	change_hit
147	Can delete hit	37	delete_hit
148	Can view hit	37	view_hit
149	Can add hit count	38	add_hitcount
150	Can change hit count	38	change_hitcount
151	Can delete hit count	38	delete_hitcount
152	Can view hit count	38	view_hitcount
\.


--
-- Data for Name: authtoken_token; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.authtoken_token (key, created, user_id) FROM stdin;
49dd11ebe24e24e20aaef57281c03fb5f4f12a66	2020-09-08 05:26:58.411511-04	2
ee05b0641ba50df3d8b2e88d98fa06c29d92ddb9	2020-09-08 05:31:01.276138-04	1
3a101cacfa36a84a2e8b903eb2d7e138c4af11d1	2020-09-08 05:32:32.025098-04	3
\.


--
-- Data for Name: blog_comment; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.blog_comment (id, "timestamp", content, post_id, user_id) FROM stdin;
\.


--
-- Data for Name: blog_post; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.blog_post (id, title, short_description, content, "timestamp", thumbnail, featured, active_post, slug, author_id) FROM stdin;
\.


--
-- Data for Name: blog_post_categories; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.blog_post_categories (id, post_id, category_id) FROM stdin;
\.


--
-- Data for Name: categories_category; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.categories_category (id, title, sub_category_of_id) FROM stdin;
1	Toy  Cars	1
2	Action Figure	1
3	Sharing Pack	2
4	Jet Printer	3
5	Label Maker	2
\.


--
-- Data for Name: categories_categoryvariation; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.categories_categoryvariation (id, value, attachment, selectable, yes_or_no, variation_id) FROM stdin;
\.


--
-- Data for Name: categories_maincategory; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.categories_maincategory (id, title) FROM stdin;
1	Toy
2	Packing Products
3	Printing Products
\.


--
-- Data for Name: categories_variation; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.categories_variation (id, name, category_id) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2020-09-08 07:05:56.552914-04	1	Toy	1	[{"added": {}}]	8	1
2	2020-09-08 07:05:58.385733-04	1	Toy  Cars	1	[{"added": {}}]	7	1
3	2020-09-08 07:06:17.516812-04	2	Action Figure	1	[{"added": {}}]	7	1
4	2020-09-08 07:06:29.178589-04	2	Packing Products	1	[{"added": {}}]	8	1
5	2020-09-08 07:06:34.649601-04	3	Sharing Pack	1	[{"added": {}}]	7	1
6	2020-09-08 07:06:43.221532-04	3	Printing Products	1	[{"added": {}}]	8	1
7	2020-09-08 07:06:47.540112-04	4	Jet Printer	1	[{"added": {}}]	7	1
8	2020-09-08 07:07:04.662775-04	5	Label Maker	1	[{"added": {}}]	7	1
9	2020-09-08 09:10:25.770335-04	5	gamer	3		4	1
10	2020-09-08 09:10:25.788693-04	4	wolf	3		4	1
11	2020-09-08 09:11:38.801104-04	6	jackjack	3		4	1
12	2020-09-13 18:48:22.742282-04	1	jer	1	[{"added": {}}]	6	1
13	2020-09-13 18:48:46.829355-04	1	شیرینگ پک by None	1	[{"added": {}}]	19	1
14	2020-09-13 18:49:06.518582-04	1	شیرینگ پک by None	2	[{"changed": {"fields": ["slug"]}}]	19	1
15	2020-09-13 18:51:50.202936-04	2	MetalGearSolidV by None	1	[{"added": {}}]	19	1
16	2020-09-14 10:42:05.842588-04	3	شیرینگ پک جدید by None	1	[{"added": {}}]	19	1
17	2020-09-14 11:10:13.061862-04	4	Plastic Bmw by None	1	[{"added": {}}]	19	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	auth	permission
2	auth	group
3	contenttypes	contenttype
4	users	user
5	users	profile
6	users	producerprofile
7	categories	category
8	categories	maincategory
9	categories	variation
10	categories	categoryvariation
11	blog	comment
12	blog	post
13	merchandise	orderitem
14	merchandise	order
15	merchandise	address
16	merchandise	payment
17	merchandise	coupon
18	merchandise	refund
19	products	product
20	products	variation
21	products	productvariation
22	products	productcomment
23	products	rating
24	pages	newstelleremails
25	pages	document
26	admin	logentry
27	sessions	session
28	sites	site
29	authtoken	token
30	account	emailaddress
31	account	emailconfirmation
32	socialaccount	socialaccount
33	socialaccount	socialapp
34	socialaccount	socialtoken
35	hitcount	blacklistip
36	hitcount	blacklistuseragent
37	hitcount	hit
38	hitcount	hitcount
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	categories	0001_initial	2020-09-07 18:36:06.8027-04
2	contenttypes	0001_initial	2020-09-07 18:37:28.809454-04
3	contenttypes	0002_remove_content_type_name	2020-09-07 18:37:28.885716-04
4	auth	0001_initial	2020-09-07 18:37:29.178667-04
5	auth	0002_alter_permission_name_max_length	2020-09-07 18:37:29.518901-04
6	auth	0003_alter_user_email_max_length	2020-09-07 18:37:29.546922-04
7	auth	0004_alter_user_username_opts	2020-09-07 18:37:29.572061-04
8	auth	0005_alter_user_last_login_null	2020-09-07 18:37:29.587531-04
9	auth	0006_require_contenttypes_0002	2020-09-07 18:37:29.600381-04
10	auth	0007_alter_validators_add_error_messages	2020-09-07 18:37:29.625588-04
11	auth	0008_alter_user_username_max_length	2020-09-07 18:37:29.645137-04
12	auth	0009_alter_user_last_name_max_length	2020-09-07 18:37:29.670491-04
13	auth	0010_alter_group_name_max_length	2020-09-07 18:37:29.691006-04
14	auth	0011_update_proxy_permissions	2020-09-07 18:37:29.735981-04
15	users	0001_initial	2020-09-07 18:37:30.221167-04
16	account	0001_initial	2020-09-07 18:38:35.524785-04
17	account	0002_email_max_length	2020-09-07 18:38:35.730364-04
18	admin	0001_initial	2020-09-07 18:38:35.851809-04
19	admin	0002_logentry_remove_auto_add	2020-09-07 18:38:35.984868-04
20	admin	0003_logentry_add_action_flag_choices	2020-09-07 18:38:36.015576-04
21	authtoken	0001_initial	2020-09-07 18:38:36.13962-04
22	authtoken	0002_auto_20160226_1747	2020-09-07 18:38:36.331704-04
23	hitcount	0001_initial	2020-09-07 18:38:36.756999-04
24	hitcount	0002_index_ip_and_session	2020-09-07 18:38:37.286977-04
25	hitcount	0003_auto_20190608_1004	2020-09-07 18:38:37.475058-04
26	hitcount	0004_auto_20200704_0933	2020-09-07 18:38:37.633159-04
27	sessions	0001_initial	2020-09-07 18:38:37.755204-04
28	sites	0001_initial	2020-09-07 18:38:37.878676-04
29	sites	0002_alter_domain_unique	2020-09-07 18:38:37.979698-04
30	socialaccount	0001_initial	2020-09-07 18:38:38.437711-04
31	socialaccount	0002_token_max_lengths	2020-09-07 18:38:38.859022-04
32	socialaccount	0003_extra_data_default_dict	2020-09-07 18:38:38.898124-04
33	products	0001_initial	2020-09-07 18:39:27.819695-04
34	merchandise	0001_initial	2020-09-07 18:40:40.206767-04
35	blog	0001_initial	2020-09-07 18:42:08.876399-04
36	pages	0001_initial	2020-09-07 18:42:27.1743-04
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
603c7pz6knpmb981g039l9duw15ai530	MzJhZWEzODI1MjhhZWFlODc4OTNlMmJmZTY2ZDY5MzVhY2NmNDFjYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5OWVmM2QxYzY2YWMzNjg4MDdmZjczYjQ3MGRiNjYyNWI3YzM5NDM3In0=	2020-09-22 08:58:10.357648-04
b9kfwpbhkk84wvmzjo6i7nmi5x1323iu	NTcyYzAyMDNmNTQwNTMzMGNlYTFkMzZlMDQ5YTIyMzkyOTc5MjRhMjp7fQ==	2020-09-22 09:03:35.731854-04
r7w0sbmheets0qc0325fhv1cdsplqsxu	NTcyYzAyMDNmNTQwNTMzMGNlYTFkMzZlMDQ5YTIyMzkyOTc5MjRhMjp7fQ==	2020-09-22 09:09:25.096452-04
kmd8komnh9vr3zjpmfu2rcb3jdf6025k	NTcyYzAyMDNmNTQwNTMzMGNlYTFkMzZlMDQ5YTIyMzkyOTc5MjRhMjp7fQ==	2020-09-22 09:11:00.307526-04
rv01ueoz1q6kqzfl4qe2f6o7uewr1wtd	NTcyYzAyMDNmNTQwNTMzMGNlYTFkMzZlMDQ5YTIyMzkyOTc5MjRhMjp7fQ==	2020-09-22 09:12:11.057807-04
izezevvfn2hqjm2vs6i2hnop1deleij4	MzJhZWEzODI1MjhhZWFlODc4OTNlMmJmZTY2ZDY5MzVhY2NmNDFjYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5OWVmM2QxYzY2YWMzNjg4MDdmZjczYjQ3MGRiNjYyNWI3YzM5NDM3In0=	2020-09-27 18:46:47.099518-04
jkaoszolxutvmt2yur1t5g3ge1hsojsr	MzJhZWEzODI1MjhhZWFlODc4OTNlMmJmZTY2ZDY5MzVhY2NmNDFjYzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5OWVmM2QxYzY2YWMzNjg4MDdmZjczYjQ3MGRiNjYyNWI3YzM5NDM3In0=	2020-09-28 10:39:20.729075-04
\.


--
-- Data for Name: django_site; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.django_site (id, domain, name) FROM stdin;
1	example.com	example.com
\.


--
-- Data for Name: hitcount_blacklist_ip; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.hitcount_blacklist_ip (id, ip) FROM stdin;
\.


--
-- Data for Name: hitcount_blacklist_user_agent; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.hitcount_blacklist_user_agent (id, user_agent) FROM stdin;
\.


--
-- Data for Name: hitcount_hit; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.hitcount_hit (id, created, ip, session, user_agent, hitcount_id, user_id) FROM stdin;
\.


--
-- Data for Name: hitcount_hit_count; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.hitcount_hit_count (id, hits, modified, object_pk, content_type_id) FROM stdin;
\.


--
-- Data for Name: merchandise_address; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.merchandise_address (id, street_address, apartment_address, zip, address_type, "default", user_id) FROM stdin;
\.


--
-- Data for Name: merchandise_coupon; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.merchandise_coupon (id, code, amount) FROM stdin;
\.


--
-- Data for Name: merchandise_order; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.merchandise_order (id, ref_code, start_date, ordered_date, ordered, being_delivered, received, refund_requested, refund_granted, billing_address_id, coupon_id, payment_id, shipping_address_id, user_id) FROM stdin;
\.


--
-- Data for Name: merchandise_order_items; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.merchandise_order_items (id, order_id, orderitem_id) FROM stdin;
\.


--
-- Data for Name: merchandise_order_producer; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.merchandise_order_producer (id, order_id, producerprofile_id) FROM stdin;
\.


--
-- Data for Name: merchandise_orderitem; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.merchandise_orderitem (id, ordered, quantity, item_id, user_id) FROM stdin;
\.


--
-- Data for Name: merchandise_payment; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.merchandise_payment (id, stripe_charge_id, amount, "timestamp", user_id) FROM stdin;
\.


--
-- Data for Name: merchandise_refund; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.merchandise_refund (id, reason, accepted, email, order_id) FROM stdin;
\.


--
-- Data for Name: pages_document; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.pages_document (id, name, document, uploaded_at) FROM stdin;
\.


--
-- Data for Name: pages_newstelleremails; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.pages_newstelleremails (id, email, user_id) FROM stdin;
\.


--
-- Data for Name: products_product; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.products_product (id, title, price, discount_price, product_image, slug, stock, description, minimum_order, payment_type, packing, shipping, origin, made_in, delivery, samples, remarks, producer_id) FROM stdin;
1	شیرینگ پک	\N	\N			5	<p>شستن این لعنتی</p>	\N	\N	\N	\N	\N	\N	\N	\N		1
2	MetalGearSolidV	\N	\N		metalgearsolidv	1	<p>sdasd</p>	\N	\N	\N	\N	\N	\N	\N	\N		1
3	شیرینگ پک جدید	\N	\N			1	<p>شت</p>	\N	\N	\N	\N	\N	\N	\N	\N		1
4	Plastic Bmw	\N	\N		plastic-bmw	4	<p>deaed</p>	\N	\N	\N	\N	\N	\N	\N	\N		1
\.


--
-- Data for Name: products_product_category; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.products_product_category (id, product_id, category_id) FROM stdin;
1	1	3
2	2	2
3	3	3
4	4	1
\.


--
-- Data for Name: products_productcomment; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.products_productcomment (id, is_confirmed, content, product_id, user_id) FROM stdin;
\.


--
-- Data for Name: products_productvariation; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.products_productvariation (id, value, attachment, variation_id) FROM stdin;
\.


--
-- Data for Name: products_rating; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.products_rating (id, stars, product_id, user_id) FROM stdin;
\.


--
-- Data for Name: products_variation; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.products_variation (id, name, product_id) FROM stdin;
\.


--
-- Data for Name: socialaccount_socialaccount; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.socialaccount_socialaccount (id, provider, uid, last_login, date_joined, extra_data, user_id) FROM stdin;
\.


--
-- Data for Name: socialaccount_socialapp; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.socialaccount_socialapp (id, provider, name, client_id, secret, key) FROM stdin;
\.


--
-- Data for Name: socialaccount_socialapp_sites; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.socialaccount_socialapp_sites (id, socialapp_id, site_id) FROM stdin;
\.


--
-- Data for Name: socialaccount_socialtoken; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.socialaccount_socialtoken (id, token, token_secret, expires_at, account_id, app_id) FROM stdin;
\.


--
-- Data for Name: users_producerprofile; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.users_producerprofile (profile_ptr_id, department, job_title, postal_code, alternative_phone, fax_number, business_type) FROM stdin;
1	\N	\N	\N	\N	\N	\N
\.


--
-- Data for Name: users_producerprofile_categoty; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.users_producerprofile_categoty (id, producerprofile_id, category_id) FROM stdin;
1	1	2
2	1	3
3	1	4
\.


--
-- Data for Name: users_profile; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.users_profile (id, gender, profile_picture, province, city, company_name, phone_number, company_address, office_address, office_phone_num, introduce_yourself, description, date_created_at, web_site, user_id) FROM stdin;
1	خانم		\N	\N	\N	\N			\N			2020-09-13 18:48:22.572681-04	\N	1
\.


--
-- Data for Name: users_user; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.users_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, is_producer, role) FROM stdin;
2	pbkdf2_sha256$150000$4k99DmGAAEzD$urW+YJu8vJ07tdDTjcFf532ZN4ulbch2jTXVs9W+ldc=	2020-09-08 05:26:58.53136-04	f	track			alire@yahoo.com	f	t	2020-09-08 05:26:58.01492-04	f	\N
3	pbkdf2_sha256$150000$3LoEBJRlpLfx$OQghyLb7zu+AjYoXNVkuytCg0n0g4FWxtfG3KIm/xIQ=	2020-09-08 05:32:32.117709-04	f	trech			aeaef@track.com	f	t	2020-09-08 05:32:31.795377-04	f	\N
7	hellomother1@	2020-09-08 09:12:11.065872-04	f	jacke			jackey@model.com	f	t	2020-09-08 09:12:11.01735-04	f	\N
1	pbkdf2_sha256$150000$wyKRB9xl8Eok$HaboE7DIRBXtnj60Z59xv19xO8PxWl840cZxDQqqybc=	2020-09-14 10:39:20.661154-04	t	jer				t	t	2020-09-07 18:42:50.178253-04	f	\N
\.


--
-- Data for Name: users_user_groups; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.users_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: users_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: jeremih
--

COPY public.users_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: account_emailaddress_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.account_emailaddress_id_seq', 2, true);


--
-- Name: account_emailconfirmation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.account_emailconfirmation_id_seq', 1, false);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 152, true);


--
-- Name: blog_comment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.blog_comment_id_seq', 1, false);


--
-- Name: blog_post_categories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.blog_post_categories_id_seq', 1, false);


--
-- Name: blog_post_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.blog_post_id_seq', 1, false);


--
-- Name: categories_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.categories_category_id_seq', 5, true);


--
-- Name: categories_categoryvariation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.categories_categoryvariation_id_seq', 1, false);


--
-- Name: categories_maincategory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.categories_maincategory_id_seq', 3, true);


--
-- Name: categories_variation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.categories_variation_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 17, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 38, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 36, true);


--
-- Name: django_site_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.django_site_id_seq', 1, true);


--
-- Name: hitcount_blacklist_ip_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.hitcount_blacklist_ip_id_seq', 1, false);


--
-- Name: hitcount_blacklist_user_agent_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.hitcount_blacklist_user_agent_id_seq', 1, false);


--
-- Name: hitcount_hit_count_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.hitcount_hit_count_id_seq', 1, false);


--
-- Name: hitcount_hit_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.hitcount_hit_id_seq', 1, false);


--
-- Name: merchandise_address_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.merchandise_address_id_seq', 1, false);


--
-- Name: merchandise_coupon_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.merchandise_coupon_id_seq', 1, false);


--
-- Name: merchandise_order_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.merchandise_order_id_seq', 1, false);


--
-- Name: merchandise_order_items_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.merchandise_order_items_id_seq', 1, false);


--
-- Name: merchandise_order_producer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.merchandise_order_producer_id_seq', 1, false);


--
-- Name: merchandise_orderitem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.merchandise_orderitem_id_seq', 1, false);


--
-- Name: merchandise_payment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.merchandise_payment_id_seq', 1, false);


--
-- Name: merchandise_refund_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.merchandise_refund_id_seq', 1, false);


--
-- Name: pages_document_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.pages_document_id_seq', 1, false);


--
-- Name: pages_newstelleremails_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.pages_newstelleremails_id_seq', 1, false);


--
-- Name: products_product_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.products_product_category_id_seq', 4, true);


--
-- Name: products_product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.products_product_id_seq', 4, true);


--
-- Name: products_productcomment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.products_productcomment_id_seq', 1, false);


--
-- Name: products_productvariation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.products_productvariation_id_seq', 1, false);


--
-- Name: products_rating_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.products_rating_id_seq', 1, false);


--
-- Name: products_variation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.products_variation_id_seq', 1, false);


--
-- Name: socialaccount_socialaccount_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.socialaccount_socialaccount_id_seq', 1, false);


--
-- Name: socialaccount_socialapp_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.socialaccount_socialapp_id_seq', 1, false);


--
-- Name: socialaccount_socialapp_sites_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.socialaccount_socialapp_sites_id_seq', 1, false);


--
-- Name: socialaccount_socialtoken_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.socialaccount_socialtoken_id_seq', 1, false);


--
-- Name: users_producerprofile_categoty_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.users_producerprofile_categoty_id_seq', 3, true);


--
-- Name: users_profile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.users_profile_id_seq', 1, true);


--
-- Name: users_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.users_user_groups_id_seq', 1, false);


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.users_user_id_seq', 7, true);


--
-- Name: users_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jeremih
--

SELECT pg_catalog.setval('public.users_user_user_permissions_id_seq', 1, false);


--
-- Name: account_emailaddress account_emailaddress_email_key; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.account_emailaddress
    ADD CONSTRAINT account_emailaddress_email_key UNIQUE (email);


--
-- Name: account_emailaddress account_emailaddress_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.account_emailaddress
    ADD CONSTRAINT account_emailaddress_pkey PRIMARY KEY (id);


--
-- Name: account_emailconfirmation account_emailconfirmation_key_key; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.account_emailconfirmation
    ADD CONSTRAINT account_emailconfirmation_key_key UNIQUE (key);


--
-- Name: account_emailconfirmation account_emailconfirmation_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.account_emailconfirmation
    ADD CONSTRAINT account_emailconfirmation_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: authtoken_token authtoken_token_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_pkey PRIMARY KEY (key);


--
-- Name: authtoken_token authtoken_token_user_id_key; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_key UNIQUE (user_id);


--
-- Name: blog_comment blog_comment_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.blog_comment
    ADD CONSTRAINT blog_comment_pkey PRIMARY KEY (id);


--
-- Name: blog_post_categories blog_post_categories_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.blog_post_categories
    ADD CONSTRAINT blog_post_categories_pkey PRIMARY KEY (id);


--
-- Name: blog_post_categories blog_post_categories_post_id_category_id_ed4f1727_uniq; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.blog_post_categories
    ADD CONSTRAINT blog_post_categories_post_id_category_id_ed4f1727_uniq UNIQUE (post_id, category_id);


--
-- Name: blog_post blog_post_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.blog_post
    ADD CONSTRAINT blog_post_pkey PRIMARY KEY (id);


--
-- Name: categories_category categories_category_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.categories_category
    ADD CONSTRAINT categories_category_pkey PRIMARY KEY (id);


--
-- Name: categories_categoryvariation categories_categoryvariation_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.categories_categoryvariation
    ADD CONSTRAINT categories_categoryvariation_pkey PRIMARY KEY (id);


--
-- Name: categories_categoryvariation categories_categoryvariation_variation_id_value_856d3cc7_uniq; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.categories_categoryvariation
    ADD CONSTRAINT categories_categoryvariation_variation_id_value_856d3cc7_uniq UNIQUE (variation_id, value);


--
-- Name: categories_maincategory categories_maincategory_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.categories_maincategory
    ADD CONSTRAINT categories_maincategory_pkey PRIMARY KEY (id);


--
-- Name: categories_variation categories_variation_category_id_name_0e6a0484_uniq; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.categories_variation
    ADD CONSTRAINT categories_variation_category_id_name_0e6a0484_uniq UNIQUE (category_id, name);


--
-- Name: categories_variation categories_variation_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.categories_variation
    ADD CONSTRAINT categories_variation_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: django_site django_site_domain_a2e37b91_uniq; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.django_site
    ADD CONSTRAINT django_site_domain_a2e37b91_uniq UNIQUE (domain);


--
-- Name: django_site django_site_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.django_site
    ADD CONSTRAINT django_site_pkey PRIMARY KEY (id);


--
-- Name: hitcount_blacklist_ip hitcount_blacklist_ip_ip_key; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.hitcount_blacklist_ip
    ADD CONSTRAINT hitcount_blacklist_ip_ip_key UNIQUE (ip);


--
-- Name: hitcount_blacklist_ip hitcount_blacklist_ip_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.hitcount_blacklist_ip
    ADD CONSTRAINT hitcount_blacklist_ip_pkey PRIMARY KEY (id);


--
-- Name: hitcount_blacklist_user_agent hitcount_blacklist_user_agent_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.hitcount_blacklist_user_agent
    ADD CONSTRAINT hitcount_blacklist_user_agent_pkey PRIMARY KEY (id);


--
-- Name: hitcount_blacklist_user_agent hitcount_blacklist_user_agent_user_agent_key; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.hitcount_blacklist_user_agent
    ADD CONSTRAINT hitcount_blacklist_user_agent_user_agent_key UNIQUE (user_agent);


--
-- Name: hitcount_hit_count hitcount_hit_count_content_type_id_object_pk_4dacb610_uniq; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.hitcount_hit_count
    ADD CONSTRAINT hitcount_hit_count_content_type_id_object_pk_4dacb610_uniq UNIQUE (content_type_id, object_pk);


--
-- Name: hitcount_hit_count hitcount_hit_count_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.hitcount_hit_count
    ADD CONSTRAINT hitcount_hit_count_pkey PRIMARY KEY (id);


--
-- Name: hitcount_hit hitcount_hit_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.hitcount_hit
    ADD CONSTRAINT hitcount_hit_pkey PRIMARY KEY (id);


--
-- Name: merchandise_address merchandise_address_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.merchandise_address
    ADD CONSTRAINT merchandise_address_pkey PRIMARY KEY (id);


--
-- Name: merchandise_coupon merchandise_coupon_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.merchandise_coupon
    ADD CONSTRAINT merchandise_coupon_pkey PRIMARY KEY (id);


--
-- Name: merchandise_order_items merchandise_order_items_order_id_orderitem_id_80ee5b43_uniq; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.merchandise_order_items
    ADD CONSTRAINT merchandise_order_items_order_id_orderitem_id_80ee5b43_uniq UNIQUE (order_id, orderitem_id);


--
-- Name: merchandise_order_items merchandise_order_items_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.merchandise_order_items
    ADD CONSTRAINT merchandise_order_items_pkey PRIMARY KEY (id);


--
-- Name: merchandise_order merchandise_order_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.merchandise_order
    ADD CONSTRAINT merchandise_order_pkey PRIMARY KEY (id);


--
-- Name: merchandise_order_producer merchandise_order_produc_order_id_producerprofile_7483381f_uniq; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.merchandise_order_producer
    ADD CONSTRAINT merchandise_order_produc_order_id_producerprofile_7483381f_uniq UNIQUE (order_id, producerprofile_id);


--
-- Name: merchandise_order_producer merchandise_order_producer_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.merchandise_order_producer
    ADD CONSTRAINT merchandise_order_producer_pkey PRIMARY KEY (id);


--
-- Name: merchandise_orderitem merchandise_orderitem_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.merchandise_orderitem
    ADD CONSTRAINT merchandise_orderitem_pkey PRIMARY KEY (id);


--
-- Name: merchandise_payment merchandise_payment_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.merchandise_payment
    ADD CONSTRAINT merchandise_payment_pkey PRIMARY KEY (id);


--
-- Name: merchandise_refund merchandise_refund_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.merchandise_refund
    ADD CONSTRAINT merchandise_refund_pkey PRIMARY KEY (id);


--
-- Name: pages_document pages_document_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.pages_document
    ADD CONSTRAINT pages_document_pkey PRIMARY KEY (id);


--
-- Name: pages_newstelleremails pages_newstelleremails_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.pages_newstelleremails
    ADD CONSTRAINT pages_newstelleremails_pkey PRIMARY KEY (id);


--
-- Name: products_product_category products_product_category_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.products_product_category
    ADD CONSTRAINT products_product_category_pkey PRIMARY KEY (id);


--
-- Name: products_product_category products_product_category_product_id_category_id_99b99489_uniq; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.products_product_category
    ADD CONSTRAINT products_product_category_product_id_category_id_99b99489_uniq UNIQUE (product_id, category_id);


--
-- Name: products_product products_product_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.products_product
    ADD CONSTRAINT products_product_pkey PRIMARY KEY (id);


--
-- Name: products_productcomment products_productcomment_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.products_productcomment
    ADD CONSTRAINT products_productcomment_pkey PRIMARY KEY (id);


--
-- Name: products_productvariation products_productvariation_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.products_productvariation
    ADD CONSTRAINT products_productvariation_pkey PRIMARY KEY (id);


--
-- Name: products_productvariation products_productvariation_variation_id_value_bb575a97_uniq; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.products_productvariation
    ADD CONSTRAINT products_productvariation_variation_id_value_bb575a97_uniq UNIQUE (variation_id, value);


--
-- Name: products_rating products_rating_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.products_rating
    ADD CONSTRAINT products_rating_pkey PRIMARY KEY (id);


--
-- Name: products_rating products_rating_user_id_product_id_d1e502eb_uniq; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.products_rating
    ADD CONSTRAINT products_rating_user_id_product_id_d1e502eb_uniq UNIQUE (user_id, product_id);


--
-- Name: products_variation products_variation_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.products_variation
    ADD CONSTRAINT products_variation_pkey PRIMARY KEY (id);


--
-- Name: products_variation products_variation_product_id_name_4c6a1fbb_uniq; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.products_variation
    ADD CONSTRAINT products_variation_product_id_name_4c6a1fbb_uniq UNIQUE (product_id, name);


--
-- Name: socialaccount_socialaccount socialaccount_socialaccount_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.socialaccount_socialaccount
    ADD CONSTRAINT socialaccount_socialaccount_pkey PRIMARY KEY (id);


--
-- Name: socialaccount_socialaccount socialaccount_socialaccount_provider_uid_fc810c6e_uniq; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.socialaccount_socialaccount
    ADD CONSTRAINT socialaccount_socialaccount_provider_uid_fc810c6e_uniq UNIQUE (provider, uid);


--
-- Name: socialaccount_socialapp_sites socialaccount_socialapp__socialapp_id_site_id_71a9a768_uniq; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.socialaccount_socialapp_sites
    ADD CONSTRAINT socialaccount_socialapp__socialapp_id_site_id_71a9a768_uniq UNIQUE (socialapp_id, site_id);


--
-- Name: socialaccount_socialapp socialaccount_socialapp_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.socialaccount_socialapp
    ADD CONSTRAINT socialaccount_socialapp_pkey PRIMARY KEY (id);


--
-- Name: socialaccount_socialapp_sites socialaccount_socialapp_sites_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.socialaccount_socialapp_sites
    ADD CONSTRAINT socialaccount_socialapp_sites_pkey PRIMARY KEY (id);


--
-- Name: socialaccount_socialtoken socialaccount_socialtoken_app_id_account_id_fca4e0ac_uniq; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.socialaccount_socialtoken
    ADD CONSTRAINT socialaccount_socialtoken_app_id_account_id_fca4e0ac_uniq UNIQUE (app_id, account_id);


--
-- Name: socialaccount_socialtoken socialaccount_socialtoken_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.socialaccount_socialtoken
    ADD CONSTRAINT socialaccount_socialtoken_pkey PRIMARY KEY (id);


--
-- Name: users_producerprofile_categoty users_producerprofile_ca_producerprofile_id_categ_08b2d963_uniq; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.users_producerprofile_categoty
    ADD CONSTRAINT users_producerprofile_ca_producerprofile_id_categ_08b2d963_uniq UNIQUE (producerprofile_id, category_id);


--
-- Name: users_producerprofile_categoty users_producerprofile_categoty_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.users_producerprofile_categoty
    ADD CONSTRAINT users_producerprofile_categoty_pkey PRIMARY KEY (id);


--
-- Name: users_producerprofile users_producerprofile_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.users_producerprofile
    ADD CONSTRAINT users_producerprofile_pkey PRIMARY KEY (profile_ptr_id);


--
-- Name: users_profile users_profile_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.users_profile
    ADD CONSTRAINT users_profile_pkey PRIMARY KEY (id);


--
-- Name: users_user_groups users_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.users_user_groups
    ADD CONSTRAINT users_user_groups_pkey PRIMARY KEY (id);


--
-- Name: users_user_groups users_user_groups_user_id_group_id_b88eab82_uniq; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.users_user_groups
    ADD CONSTRAINT users_user_groups_user_id_group_id_b88eab82_uniq UNIQUE (user_id, group_id);


--
-- Name: users_user users_user_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.users_user
    ADD CONSTRAINT users_user_pkey PRIMARY KEY (id);


--
-- Name: users_user_user_permissions users_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.users_user_user_permissions
    ADD CONSTRAINT users_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: users_user_user_permissions users_user_user_permissions_user_id_permission_id_43338c45_uniq; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.users_user_user_permissions
    ADD CONSTRAINT users_user_user_permissions_user_id_permission_id_43338c45_uniq UNIQUE (user_id, permission_id);


--
-- Name: users_user users_user_username_key; Type: CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.users_user
    ADD CONSTRAINT users_user_username_key UNIQUE (username);


--
-- Name: account_emailaddress_email_03be32b2_like; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX account_emailaddress_email_03be32b2_like ON public.account_emailaddress USING btree (email varchar_pattern_ops);


--
-- Name: account_emailaddress_user_id_2c513194; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX account_emailaddress_user_id_2c513194 ON public.account_emailaddress USING btree (user_id);


--
-- Name: account_emailconfirmation_email_address_id_5b7f8c58; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX account_emailconfirmation_email_address_id_5b7f8c58 ON public.account_emailconfirmation USING btree (email_address_id);


--
-- Name: account_emailconfirmation_key_f43612bd_like; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX account_emailconfirmation_key_f43612bd_like ON public.account_emailconfirmation USING btree (key varchar_pattern_ops);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: authtoken_token_key_10f0b77e_like; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX authtoken_token_key_10f0b77e_like ON public.authtoken_token USING btree (key varchar_pattern_ops);


--
-- Name: blog_comment_post_id_580e96ef; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX blog_comment_post_id_580e96ef ON public.blog_comment USING btree (post_id);


--
-- Name: blog_comment_user_id_59a54155; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX blog_comment_user_id_59a54155 ON public.blog_comment USING btree (user_id);


--
-- Name: blog_post_author_id_dd7a8485; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX blog_post_author_id_dd7a8485 ON public.blog_post USING btree (author_id);


--
-- Name: blog_post_categories_category_id_2211dae5; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX blog_post_categories_category_id_2211dae5 ON public.blog_post_categories USING btree (category_id);


--
-- Name: blog_post_categories_post_id_c34e7be1; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX blog_post_categories_post_id_c34e7be1 ON public.blog_post_categories USING btree (post_id);


--
-- Name: blog_post_slug_b95473f2; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX blog_post_slug_b95473f2 ON public.blog_post USING btree (slug);


--
-- Name: blog_post_slug_b95473f2_like; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX blog_post_slug_b95473f2_like ON public.blog_post USING btree (slug varchar_pattern_ops);


--
-- Name: categories_category_sub_category_of_id_72576107; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX categories_category_sub_category_of_id_72576107 ON public.categories_category USING btree (sub_category_of_id);


--
-- Name: categories_categoryvariation_variation_id_e66ef9ae; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX categories_categoryvariation_variation_id_e66ef9ae ON public.categories_categoryvariation USING btree (variation_id);


--
-- Name: categories_variation_category_id_a6dc6e92; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX categories_variation_category_id_a6dc6e92 ON public.categories_variation USING btree (category_id);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: django_site_domain_a2e37b91_like; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX django_site_domain_a2e37b91_like ON public.django_site USING btree (domain varchar_pattern_ops);


--
-- Name: hitcount_blacklist_ip_ip_b1955e95_like; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX hitcount_blacklist_ip_ip_b1955e95_like ON public.hitcount_blacklist_ip USING btree (ip varchar_pattern_ops);


--
-- Name: hitcount_blacklist_user_agent_user_agent_fbf2061c_like; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX hitcount_blacklist_user_agent_user_agent_fbf2061c_like ON public.hitcount_blacklist_user_agent USING btree (user_agent varchar_pattern_ops);


--
-- Name: hitcount_hit_count_content_type_id_4a734fe1; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX hitcount_hit_count_content_type_id_4a734fe1 ON public.hitcount_hit_count USING btree (content_type_id);


--
-- Name: hitcount_hit_created_79adf7bc; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX hitcount_hit_created_79adf7bc ON public.hitcount_hit USING btree (created);


--
-- Name: hitcount_hit_hitcount_id_b7971910; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX hitcount_hit_hitcount_id_b7971910 ON public.hitcount_hit USING btree (hitcount_id);


--
-- Name: hitcount_hit_ip_a52a62aa; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX hitcount_hit_ip_a52a62aa ON public.hitcount_hit USING btree (ip);


--
-- Name: hitcount_hit_ip_a52a62aa_like; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX hitcount_hit_ip_a52a62aa_like ON public.hitcount_hit USING btree (ip varchar_pattern_ops);


--
-- Name: hitcount_hit_session_5be83758; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX hitcount_hit_session_5be83758 ON public.hitcount_hit USING btree (session);


--
-- Name: hitcount_hit_session_5be83758_like; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX hitcount_hit_session_5be83758_like ON public.hitcount_hit USING btree (session varchar_pattern_ops);


--
-- Name: hitcount_hit_user_id_f7067f66; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX hitcount_hit_user_id_f7067f66 ON public.hitcount_hit USING btree (user_id);


--
-- Name: merchandise_address_user_id_2c26b7e2; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX merchandise_address_user_id_2c26b7e2 ON public.merchandise_address USING btree (user_id);


--
-- Name: merchandise_order_billing_address_id_d8be1c1d; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX merchandise_order_billing_address_id_d8be1c1d ON public.merchandise_order USING btree (billing_address_id);


--
-- Name: merchandise_order_coupon_id_cada80de; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX merchandise_order_coupon_id_cada80de ON public.merchandise_order USING btree (coupon_id);


--
-- Name: merchandise_order_items_order_id_6c0860c8; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX merchandise_order_items_order_id_6c0860c8 ON public.merchandise_order_items USING btree (order_id);


--
-- Name: merchandise_order_items_orderitem_id_4bd245ea; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX merchandise_order_items_orderitem_id_4bd245ea ON public.merchandise_order_items USING btree (orderitem_id);


--
-- Name: merchandise_order_payment_id_925be8d7; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX merchandise_order_payment_id_925be8d7 ON public.merchandise_order USING btree (payment_id);


--
-- Name: merchandise_order_producer_order_id_bca3755e; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX merchandise_order_producer_order_id_bca3755e ON public.merchandise_order_producer USING btree (order_id);


--
-- Name: merchandise_order_producer_producerprofile_id_b83cb66a; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX merchandise_order_producer_producerprofile_id_b83cb66a ON public.merchandise_order_producer USING btree (producerprofile_id);


--
-- Name: merchandise_order_shipping_address_id_b99f4678; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX merchandise_order_shipping_address_id_b99f4678 ON public.merchandise_order USING btree (shipping_address_id);


--
-- Name: merchandise_order_user_id_fa8c8878; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX merchandise_order_user_id_fa8c8878 ON public.merchandise_order USING btree (user_id);


--
-- Name: merchandise_orderitem_item_id_0b1de3f9; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX merchandise_orderitem_item_id_0b1de3f9 ON public.merchandise_orderitem USING btree (item_id);


--
-- Name: merchandise_orderitem_user_id_2b363bf7; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX merchandise_orderitem_user_id_2b363bf7 ON public.merchandise_orderitem USING btree (user_id);


--
-- Name: merchandise_payment_user_id_f0559efd; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX merchandise_payment_user_id_f0559efd ON public.merchandise_payment USING btree (user_id);


--
-- Name: merchandise_refund_order_id_b6047679; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX merchandise_refund_order_id_b6047679 ON public.merchandise_refund USING btree (order_id);


--
-- Name: pages_newstelleremails_user_id_3cd19fae; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX pages_newstelleremails_user_id_3cd19fae ON public.pages_newstelleremails USING btree (user_id);


--
-- Name: products_product_category_category_id_6bd7b606; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX products_product_category_category_id_6bd7b606 ON public.products_product_category USING btree (category_id);


--
-- Name: products_product_category_product_id_08fb2842; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX products_product_category_product_id_08fb2842 ON public.products_product_category USING btree (product_id);


--
-- Name: products_product_producer_id_be45bf24; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX products_product_producer_id_be45bf24 ON public.products_product USING btree (producer_id);


--
-- Name: products_product_slug_70d3148d; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX products_product_slug_70d3148d ON public.products_product USING btree (slug);


--
-- Name: products_product_slug_70d3148d_like; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX products_product_slug_70d3148d_like ON public.products_product USING btree (slug varchar_pattern_ops);


--
-- Name: products_productcomment_product_id_1e45f07c; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX products_productcomment_product_id_1e45f07c ON public.products_productcomment USING btree (product_id);


--
-- Name: products_productcomment_user_id_29c59a46; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX products_productcomment_user_id_29c59a46 ON public.products_productcomment USING btree (user_id);


--
-- Name: products_productvariation_variation_id_3abec4ae; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX products_productvariation_variation_id_3abec4ae ON public.products_productvariation USING btree (variation_id);


--
-- Name: products_rating_product_id_f60bd2d8; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX products_rating_product_id_f60bd2d8 ON public.products_rating USING btree (product_id);


--
-- Name: products_rating_user_id_f9283a7e; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX products_rating_user_id_f9283a7e ON public.products_rating USING btree (user_id);


--
-- Name: products_rating_user_id_product_id_d1e502eb_idx; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX products_rating_user_id_product_id_d1e502eb_idx ON public.products_rating USING btree (user_id, product_id);


--
-- Name: products_variation_product_id_58e457dc; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX products_variation_product_id_58e457dc ON public.products_variation USING btree (product_id);


--
-- Name: socialaccount_socialaccount_user_id_8146e70c; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX socialaccount_socialaccount_user_id_8146e70c ON public.socialaccount_socialaccount USING btree (user_id);


--
-- Name: socialaccount_socialapp_sites_site_id_2579dee5; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX socialaccount_socialapp_sites_site_id_2579dee5 ON public.socialaccount_socialapp_sites USING btree (site_id);


--
-- Name: socialaccount_socialapp_sites_socialapp_id_97fb6e7d; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX socialaccount_socialapp_sites_socialapp_id_97fb6e7d ON public.socialaccount_socialapp_sites USING btree (socialapp_id);


--
-- Name: socialaccount_socialtoken_account_id_951f210e; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX socialaccount_socialtoken_account_id_951f210e ON public.socialaccount_socialtoken USING btree (account_id);


--
-- Name: socialaccount_socialtoken_app_id_636a42d7; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX socialaccount_socialtoken_app_id_636a42d7 ON public.socialaccount_socialtoken USING btree (app_id);


--
-- Name: users_producerprofile_categoty_category_id_4b393d42; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX users_producerprofile_categoty_category_id_4b393d42 ON public.users_producerprofile_categoty USING btree (category_id);


--
-- Name: users_producerprofile_categoty_producerprofile_id_62622dda; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX users_producerprofile_categoty_producerprofile_id_62622dda ON public.users_producerprofile_categoty USING btree (producerprofile_id);


--
-- Name: users_profile_user_id_2112e78d; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX users_profile_user_id_2112e78d ON public.users_profile USING btree (user_id);


--
-- Name: users_user_groups_group_id_9afc8d0e; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX users_user_groups_group_id_9afc8d0e ON public.users_user_groups USING btree (group_id);


--
-- Name: users_user_groups_user_id_5f6f5a90; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX users_user_groups_user_id_5f6f5a90 ON public.users_user_groups USING btree (user_id);


--
-- Name: users_user_user_permissions_permission_id_0b93982e; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX users_user_user_permissions_permission_id_0b93982e ON public.users_user_user_permissions USING btree (permission_id);


--
-- Name: users_user_user_permissions_user_id_20aca447; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX users_user_user_permissions_user_id_20aca447 ON public.users_user_user_permissions USING btree (user_id);


--
-- Name: users_user_username_06e46fe6_like; Type: INDEX; Schema: public; Owner: jeremih
--

CREATE INDEX users_user_username_06e46fe6_like ON public.users_user USING btree (username varchar_pattern_ops);


--
-- Name: account_emailaddress account_emailaddress_user_id_2c513194_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.account_emailaddress
    ADD CONSTRAINT account_emailaddress_user_id_2c513194_fk_users_user_id FOREIGN KEY (user_id) REFERENCES public.users_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_emailconfirmation account_emailconfirm_email_address_id_5b7f8c58_fk_account_e; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.account_emailconfirmation
    ADD CONSTRAINT account_emailconfirm_email_address_id_5b7f8c58_fk_account_e FOREIGN KEY (email_address_id) REFERENCES public.account_emailaddress(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: authtoken_token authtoken_token_user_id_35299eff_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_35299eff_fk_users_user_id FOREIGN KEY (user_id) REFERENCES public.users_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: blog_comment blog_comment_post_id_580e96ef_fk_blog_post_id; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.blog_comment
    ADD CONSTRAINT blog_comment_post_id_580e96ef_fk_blog_post_id FOREIGN KEY (post_id) REFERENCES public.blog_post(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: blog_comment blog_comment_user_id_59a54155_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.blog_comment
    ADD CONSTRAINT blog_comment_user_id_59a54155_fk_users_user_id FOREIGN KEY (user_id) REFERENCES public.users_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: blog_post blog_post_author_id_dd7a8485_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.blog_post
    ADD CONSTRAINT blog_post_author_id_dd7a8485_fk_users_user_id FOREIGN KEY (author_id) REFERENCES public.users_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: blog_post_categories blog_post_categories_category_id_2211dae5_fk_categorie; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.blog_post_categories
    ADD CONSTRAINT blog_post_categories_category_id_2211dae5_fk_categorie FOREIGN KEY (category_id) REFERENCES public.categories_category(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: blog_post_categories blog_post_categories_post_id_c34e7be1_fk_blog_post_id; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.blog_post_categories
    ADD CONSTRAINT blog_post_categories_post_id_c34e7be1_fk_blog_post_id FOREIGN KEY (post_id) REFERENCES public.blog_post(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: categories_category categories_category_sub_category_of_id_72576107_fk_categorie; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.categories_category
    ADD CONSTRAINT categories_category_sub_category_of_id_72576107_fk_categorie FOREIGN KEY (sub_category_of_id) REFERENCES public.categories_maincategory(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: categories_categoryvariation categories_categoryv_variation_id_e66ef9ae_fk_categorie; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.categories_categoryvariation
    ADD CONSTRAINT categories_categoryv_variation_id_e66ef9ae_fk_categorie FOREIGN KEY (variation_id) REFERENCES public.categories_variation(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: categories_variation categories_variation_category_id_a6dc6e92_fk_categorie; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.categories_variation
    ADD CONSTRAINT categories_variation_category_id_a6dc6e92_fk_categorie FOREIGN KEY (category_id) REFERENCES public.categories_category(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_users_user_id FOREIGN KEY (user_id) REFERENCES public.users_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: hitcount_hit_count hitcount_hit_count_content_type_id_4a734fe1_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.hitcount_hit_count
    ADD CONSTRAINT hitcount_hit_count_content_type_id_4a734fe1_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: hitcount_hit hitcount_hit_hitcount_id_b7971910_fk_hitcount_hit_count_id; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.hitcount_hit
    ADD CONSTRAINT hitcount_hit_hitcount_id_b7971910_fk_hitcount_hit_count_id FOREIGN KEY (hitcount_id) REFERENCES public.hitcount_hit_count(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: hitcount_hit hitcount_hit_user_id_f7067f66_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.hitcount_hit
    ADD CONSTRAINT hitcount_hit_user_id_f7067f66_fk_users_user_id FOREIGN KEY (user_id) REFERENCES public.users_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: merchandise_address merchandise_address_user_id_2c26b7e2_fk_users_profile_id; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.merchandise_address
    ADD CONSTRAINT merchandise_address_user_id_2c26b7e2_fk_users_profile_id FOREIGN KEY (user_id) REFERENCES public.users_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: merchandise_order merchandise_order_billing_address_id_d8be1c1d_fk_merchandi; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.merchandise_order
    ADD CONSTRAINT merchandise_order_billing_address_id_d8be1c1d_fk_merchandi FOREIGN KEY (billing_address_id) REFERENCES public.merchandise_address(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: merchandise_order merchandise_order_coupon_id_cada80de_fk_merchandise_coupon_id; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.merchandise_order
    ADD CONSTRAINT merchandise_order_coupon_id_cada80de_fk_merchandise_coupon_id FOREIGN KEY (coupon_id) REFERENCES public.merchandise_coupon(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: merchandise_order_items merchandise_order_it_order_id_6c0860c8_fk_merchandi; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.merchandise_order_items
    ADD CONSTRAINT merchandise_order_it_order_id_6c0860c8_fk_merchandi FOREIGN KEY (order_id) REFERENCES public.merchandise_order(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: merchandise_order_items merchandise_order_it_orderitem_id_4bd245ea_fk_merchandi; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.merchandise_order_items
    ADD CONSTRAINT merchandise_order_it_orderitem_id_4bd245ea_fk_merchandi FOREIGN KEY (orderitem_id) REFERENCES public.merchandise_orderitem(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: merchandise_order merchandise_order_payment_id_925be8d7_fk_merchandise_payment_id; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.merchandise_order
    ADD CONSTRAINT merchandise_order_payment_id_925be8d7_fk_merchandise_payment_id FOREIGN KEY (payment_id) REFERENCES public.merchandise_payment(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: merchandise_order_producer merchandise_order_pr_order_id_bca3755e_fk_merchandi; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.merchandise_order_producer
    ADD CONSTRAINT merchandise_order_pr_order_id_bca3755e_fk_merchandi FOREIGN KEY (order_id) REFERENCES public.merchandise_order(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: merchandise_order_producer merchandise_order_pr_producerprofile_id_b83cb66a_fk_users_pro; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.merchandise_order_producer
    ADD CONSTRAINT merchandise_order_pr_producerprofile_id_b83cb66a_fk_users_pro FOREIGN KEY (producerprofile_id) REFERENCES public.users_producerprofile(profile_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: merchandise_order merchandise_order_shipping_address_id_b99f4678_fk_merchandi; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.merchandise_order
    ADD CONSTRAINT merchandise_order_shipping_address_id_b99f4678_fk_merchandi FOREIGN KEY (shipping_address_id) REFERENCES public.merchandise_address(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: merchandise_order merchandise_order_user_id_fa8c8878_fk_users_profile_id; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.merchandise_order
    ADD CONSTRAINT merchandise_order_user_id_fa8c8878_fk_users_profile_id FOREIGN KEY (user_id) REFERENCES public.users_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: merchandise_orderitem merchandise_orderitem_item_id_0b1de3f9_fk_products_product_id; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.merchandise_orderitem
    ADD CONSTRAINT merchandise_orderitem_item_id_0b1de3f9_fk_products_product_id FOREIGN KEY (item_id) REFERENCES public.products_product(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: merchandise_orderitem merchandise_orderitem_user_id_2b363bf7_fk_users_profile_id; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.merchandise_orderitem
    ADD CONSTRAINT merchandise_orderitem_user_id_2b363bf7_fk_users_profile_id FOREIGN KEY (user_id) REFERENCES public.users_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: merchandise_payment merchandise_payment_user_id_f0559efd_fk_users_profile_id; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.merchandise_payment
    ADD CONSTRAINT merchandise_payment_user_id_f0559efd_fk_users_profile_id FOREIGN KEY (user_id) REFERENCES public.users_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: merchandise_refund merchandise_refund_order_id_b6047679_fk_merchandise_order_id; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.merchandise_refund
    ADD CONSTRAINT merchandise_refund_order_id_b6047679_fk_merchandise_order_id FOREIGN KEY (order_id) REFERENCES public.merchandise_order(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: pages_newstelleremails pages_newstelleremails_user_id_3cd19fae_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.pages_newstelleremails
    ADD CONSTRAINT pages_newstelleremails_user_id_3cd19fae_fk_users_user_id FOREIGN KEY (user_id) REFERENCES public.users_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: products_product_category products_product_cat_category_id_6bd7b606_fk_categorie; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.products_product_category
    ADD CONSTRAINT products_product_cat_category_id_6bd7b606_fk_categorie FOREIGN KEY (category_id) REFERENCES public.categories_category(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: products_product_category products_product_cat_product_id_08fb2842_fk_products_; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.products_product_category
    ADD CONSTRAINT products_product_cat_product_id_08fb2842_fk_products_ FOREIGN KEY (product_id) REFERENCES public.products_product(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: products_product products_product_producer_id_be45bf24_fk_users_pro; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.products_product
    ADD CONSTRAINT products_product_producer_id_be45bf24_fk_users_pro FOREIGN KEY (producer_id) REFERENCES public.users_producerprofile(profile_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: products_productcomment products_productcomm_product_id_1e45f07c_fk_products_; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.products_productcomment
    ADD CONSTRAINT products_productcomm_product_id_1e45f07c_fk_products_ FOREIGN KEY (product_id) REFERENCES public.products_product(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: products_productcomment products_productcomment_user_id_29c59a46_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.products_productcomment
    ADD CONSTRAINT products_productcomment_user_id_29c59a46_fk_users_user_id FOREIGN KEY (user_id) REFERENCES public.users_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: products_productvariation products_productvari_variation_id_3abec4ae_fk_products_; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.products_productvariation
    ADD CONSTRAINT products_productvari_variation_id_3abec4ae_fk_products_ FOREIGN KEY (variation_id) REFERENCES public.products_variation(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: products_rating products_rating_product_id_f60bd2d8_fk_products_product_id; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.products_rating
    ADD CONSTRAINT products_rating_product_id_f60bd2d8_fk_products_product_id FOREIGN KEY (product_id) REFERENCES public.products_product(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: products_rating products_rating_user_id_f9283a7e_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.products_rating
    ADD CONSTRAINT products_rating_user_id_f9283a7e_fk_users_user_id FOREIGN KEY (user_id) REFERENCES public.users_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: products_variation products_variation_product_id_58e457dc_fk_products_product_id; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.products_variation
    ADD CONSTRAINT products_variation_product_id_58e457dc_fk_products_product_id FOREIGN KEY (product_id) REFERENCES public.products_product(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: socialaccount_socialtoken socialaccount_social_account_id_951f210e_fk_socialacc; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.socialaccount_socialtoken
    ADD CONSTRAINT socialaccount_social_account_id_951f210e_fk_socialacc FOREIGN KEY (account_id) REFERENCES public.socialaccount_socialaccount(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: socialaccount_socialtoken socialaccount_social_app_id_636a42d7_fk_socialacc; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.socialaccount_socialtoken
    ADD CONSTRAINT socialaccount_social_app_id_636a42d7_fk_socialacc FOREIGN KEY (app_id) REFERENCES public.socialaccount_socialapp(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: socialaccount_socialapp_sites socialaccount_social_site_id_2579dee5_fk_django_si; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.socialaccount_socialapp_sites
    ADD CONSTRAINT socialaccount_social_site_id_2579dee5_fk_django_si FOREIGN KEY (site_id) REFERENCES public.django_site(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: socialaccount_socialapp_sites socialaccount_social_socialapp_id_97fb6e7d_fk_socialacc; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.socialaccount_socialapp_sites
    ADD CONSTRAINT socialaccount_social_socialapp_id_97fb6e7d_fk_socialacc FOREIGN KEY (socialapp_id) REFERENCES public.socialaccount_socialapp(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: socialaccount_socialaccount socialaccount_socialaccount_user_id_8146e70c_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.socialaccount_socialaccount
    ADD CONSTRAINT socialaccount_socialaccount_user_id_8146e70c_fk_users_user_id FOREIGN KEY (user_id) REFERENCES public.users_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_producerprofile_categoty users_producerprofil_category_id_4b393d42_fk_categorie; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.users_producerprofile_categoty
    ADD CONSTRAINT users_producerprofil_category_id_4b393d42_fk_categorie FOREIGN KEY (category_id) REFERENCES public.categories_category(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_producerprofile_categoty users_producerprofil_producerprofile_id_62622dda_fk_users_pro; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.users_producerprofile_categoty
    ADD CONSTRAINT users_producerprofil_producerprofile_id_62622dda_fk_users_pro FOREIGN KEY (producerprofile_id) REFERENCES public.users_producerprofile(profile_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_producerprofile users_producerprofil_profile_ptr_id_5a5586af_fk_users_pro; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.users_producerprofile
    ADD CONSTRAINT users_producerprofil_profile_ptr_id_5a5586af_fk_users_pro FOREIGN KEY (profile_ptr_id) REFERENCES public.users_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_profile users_profile_user_id_2112e78d_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.users_profile
    ADD CONSTRAINT users_profile_user_id_2112e78d_fk_users_user_id FOREIGN KEY (user_id) REFERENCES public.users_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_user_groups users_user_groups_group_id_9afc8d0e_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.users_user_groups
    ADD CONSTRAINT users_user_groups_group_id_9afc8d0e_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_user_groups users_user_groups_user_id_5f6f5a90_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.users_user_groups
    ADD CONSTRAINT users_user_groups_user_id_5f6f5a90_fk_users_user_id FOREIGN KEY (user_id) REFERENCES public.users_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_user_user_permissions users_user_user_perm_permission_id_0b93982e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.users_user_user_permissions
    ADD CONSTRAINT users_user_user_perm_permission_id_0b93982e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: users_user_user_permissions users_user_user_permissions_user_id_20aca447_fk_users_user_id; Type: FK CONSTRAINT; Schema: public; Owner: jeremih
--

ALTER TABLE ONLY public.users_user_user_permissions
    ADD CONSTRAINT users_user_user_permissions_user_id_20aca447_fk_users_user_id FOREIGN KEY (user_id) REFERENCES public.users_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

