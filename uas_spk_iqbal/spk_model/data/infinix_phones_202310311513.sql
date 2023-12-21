--
-- PostgreSQL database dump
--

-- Dumped from database version 16.0
-- Dumped by pg_dump version 16.0

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
-- Name: infinix_phones; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.infinix_phones (
    id integer,
    model text,
    ram integer,
    processor text,
    storage integer,
    battery integer,
    price bigint,
    screen_size real
);


ALTER TABLE public.infinix_phones OWNER TO postgres;

--
-- Data for Name: infinix_phones; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.infinix_phones (id, model, ram, processor, storage, battery, price, screen_size) FROM stdin;
1	Infinix Zero 30 5G	12	MediaTek Dimensity 8020	256	5000	4299000	6.78
2	Infinix Zero 30	8	MediaTek Helio G99	256	5000	3099000	6.78
3	Infinix GT 10 pro 5G	8	MediaTek Dimensity 8050	256	5000	3899000	6.67
4	Infinix Hot 30 Play	4	MediaTek Helio G37	64	6000	1249000	6.82
5	Infinix Note 30 Pro	8	MediaTek Helio G99	256	5000	2948000	6.67
6	Infinix Hot 30	8	MediaTek Helio G88	128	5000	1609000	6.78
7	Infinix Note 30	8	MediaTek Helio G99	256	5000	2499000	6.78
8	Infinix Hot 30 i	8	MediaTek Helio G37	128	5000	1499000	6.6
9	Infinix Smart 7	3	MediaTek Helio A22	64	5000	1149000	6.6
10	Infinix Hot 20 i	4	MediaTek Helio G37	64	5000	1599000	6.6
\.


--
-- PostgreSQL database dump complete
--

