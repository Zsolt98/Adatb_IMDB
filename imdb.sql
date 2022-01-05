-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Gép: 127.0.0.1
-- Létrehozás ideje: 2021. Nov 28. 03:08
-- Kiszolgáló verziója: 10.4.21-MariaDB
-- PHP verzió: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Adatbázis: `imdb`
--
CREATE DATABASE IF NOT EXISTS `imdb` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `imdb`;

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `film`
--

CREATE TABLE IF NOT EXISTS `film` (
  `Film_id` int(10) NOT NULL AUTO_INCREMENT,
  `Film_cim` varchar(30) NOT NULL,
  `Film_megjelenesEve` varchar(4) NOT NULL,
  `Film_jatekido` int(4) NOT NULL,
  `Film_rendezo_id` int(10) NOT NULL,
  PRIMARY KEY (`Film_id`),
  KEY `Film_rendezo_id` (`Film_rendezo_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

--
-- A tábla adatainak kiíratása `film`
--

INSERT INTO `film` (`Film_id`, `Film_cim`, `Film_megjelenesEve`, `Film_jatekido`, `Film_rendezo_id`) VALUES
(1, 'Batman v Superman', '2016', 151, 1),
(2, 'Deadpool', '2016', 108, 2),
(3, 'Furious 7', '2015', 138, 3),
(4, 'PK', '2014', 153, 4),
(5, 'Gladiator', '2000', 155, 5),
(6, 'The Hangover', '2009', 160, 6),
(7, '3 Idiots', '2009', 211, 4),
(8, 'Spectre', '2015', 148, 7),
(9, 'Batman Begins', '2005', 160, 8),
(10, 'Deadpool 2', '2018', 108, 2),
(11, 'The Dark Knight', '2008', 152, 8),
(12, 'Amerika kapitány', '2011', 122, 9),
(13, 'The Dark Knight Rises', '2012', 165, 8),
(14, 'Dirty dancing', '1987', 100, 10);

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `filmmufaj`
--

CREATE TABLE IF NOT EXISTS `filmmufaj` (
  `FilmMufaj_id` int(10) NOT NULL AUTO_INCREMENT,
  `FilmMufaj_id_Film_id` int(10) NOT NULL,
  `FilmMufaj_id_Film_mufaj_id` int(10) NOT NULL,
  PRIMARY KEY (`FilmMufaj_id`),
  KEY `FilmMufaj_id_Film_id` (`FilmMufaj_id_Film_id`),
  KEY `FilmMufaj_id_Film_mufaj_id` (`FilmMufaj_id_Film_mufaj_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

--
-- A tábla adatainak kiíratása `filmmufaj`
--

INSERT INTO `filmmufaj` (`FilmMufaj_id`, `FilmMufaj_id_Film_id`, `FilmMufaj_id_Film_mufaj_id`) VALUES
(1, 1, 1),
(2, 9, 1),
(3, 10, 1),
(4, 2, 2),
(5, 10, 2),
(6, 14, 12);

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `mufaj`
--

CREATE TABLE IF NOT EXISTS `mufaj` (
  `Mufaj_id` int(10) NOT NULL,
  `Mufaj_neve` varchar(30) NOT NULL,
  PRIMARY KEY (`Mufaj_id`),
  UNIQUE KEY `Mufaj_neve` (`Mufaj_neve`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- A tábla adatainak kiíratása `mufaj`
--

INSERT INTO `mufaj` (`Mufaj_id`, `Mufaj_neve`) VALUES
(1, 'Akció'),
(5, 'Bűnügyi'),
(4, 'Dráma'),
(11, 'Háborús'),
(6, 'Horror'),
(8, 'Katasztrófafilm'),
(3, 'Krimi'),
(9, 'Musical'),
(12, 'Romantikus'),
(7, 'Sci-fi'),
(10, 'Szuperhős'),
(2, 'Vígjáték');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `nemzetiseg`
--

CREATE TABLE IF NOT EXISTS `nemzetiseg` (
  `Nemzetiseg_id` int(10) NOT NULL AUTO_INCREMENT,
  `Nemzetiseg_neve` varchar(30) NOT NULL,
  PRIMARY KEY (`Nemzetiseg_id`),
  UNIQUE KEY `Nemzetiseg_neve` (`Nemzetiseg_neve`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

--
-- A tábla adatainak kiíratása `nemzetiseg`
--

INSERT INTO `nemzetiseg` (`Nemzetiseg_id`, `Nemzetiseg_neve`) VALUES
(1, 'Amerikai'),
(4, 'Ausztrál'),
(2, 'Brit'),
(3, 'Indiai'),
(6, 'Izrael'),
(5, 'Magyar'),
(7, 'Olasz'),
(8, 'Román');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `rendezes`
--

CREATE TABLE IF NOT EXISTS `rendezes` (
  `Rendezes_id` int(10) NOT NULL AUTO_INCREMENT,
  `Rendezes_Rendezo_id` int(10) NOT NULL,
  `Rendezes_Film_id` int(10) NOT NULL,
  PRIMARY KEY (`Rendezes_id`),
  KEY `rendezes_rendezo_id` (`Rendezes_Rendezo_id`),
  KEY `rendezes_film_id` (`Rendezes_Film_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

--
-- A tábla adatainak kiíratása `rendezes`
--

INSERT INTO `rendezes` (`Rendezes_id`, `Rendezes_Rendezo_id`, `Rendezes_Film_id`) VALUES
(1, 8, 9),
(2, 8, 11),
(3, 1, 1),
(4, 5, 5),
(5, 3, 3),
(6, 2, 2),
(7, 2, 10),
(8, 4, 5),
(11, 10, 14);

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `rendezo`
--

CREATE TABLE IF NOT EXISTS `rendezo` (
  `Rendezo_id` int(10) NOT NULL AUTO_INCREMENT,
  `Rendezo_nev` varchar(30) NOT NULL,
  `Rendezo_nemzetiseg_id` int(10) NOT NULL,
  PRIMARY KEY (`Rendezo_id`),
  KEY `Rendezo_nemzetiseg` (`Rendezo_nemzetiseg_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

--
-- A tábla adatainak kiíratása `rendezo`
--

INSERT INTO `rendezo` (`Rendezo_id`, `Rendezo_nev`, `Rendezo_nemzetiseg_id`) VALUES
(1, 'Zack Snyder', 1),
(2, 'Tim Miller', 1),
(3, 'James Wan', 4),
(4, 'Rajkumar Hirani', 3),
(5, 'Ridley Scott', 2),
(6, 'Todd Phillips', 1),
(7, 'Sam Mendes', 2),
(8, 'Christopher Nolan', 2),
(9, 'Joe Johnston', 1),
(10, 'Emile Ardolino', 1);

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `szereples`
--

CREATE TABLE IF NOT EXISTS `szereples` (
  `Szereples_id` int(10) NOT NULL AUTO_INCREMENT,
  `Szereples_szerep` varchar(30) NOT NULL,
  `Szereples_Szinesz_id` int(10) NOT NULL,
  `Szereples_Film_id` int(10) NOT NULL,
  PRIMARY KEY (`Szereples_id`),
  KEY `Szereples_Szinesz_id` (`Szereples_Szinesz_id`),
  KEY `Szereples_Film_id` (`Szereples_Film_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

--
-- A tábla adatainak kiíratása `szereples`
--

INSERT INTO `szereples` (`Szereples_id`, `Szereples_szerep`, `Szereples_Szinesz_id`, `Szereples_Film_id`) VALUES
(1, 'Batman', 1, 9),
(2, 'James Bond', 3, 8),
(3, 'Mr. Deadpool', 2, 2),
(4, 'Mr. Deadpool', 2, 10),
(5, 'Batman', 1, 11),
(6, 'Bruce Wayne', 1, 9),
(7, 'Bruce Wayne', 1, 11),
(8, 'Wonder Woman', 4, 1),
(10, 'James', 10, 12),
(11, 'Jhonny', 11, 14);

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `szinesz`
--

CREATE TABLE IF NOT EXISTS `szinesz` (
  `Szinesz_id` int(10) NOT NULL AUTO_INCREMENT,
  `Szinesz_nev` varchar(30) NOT NULL,
  `Szinesz_neme` tinyint(1) NOT NULL,
  `Szinesz_szuletes` date NOT NULL,
  `Szinesz_nemzetiseg_id` int(10) NOT NULL,
  PRIMARY KEY (`Szinesz_id`),
  KEY `szinesz_nemzetiseg_id` (`Szinesz_nemzetiseg_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

--
-- A tábla adatainak kiíratása `szinesz`
--

INSERT INTO `szinesz` (`Szinesz_id`, `Szinesz_nev`, `Szinesz_neme`, `Szinesz_szuletes`, `Szinesz_nemzetiseg_id`) VALUES
(1, 'Christian Bale', 0, '1974-01-30', 2),
(2, 'Ryan Reynolds', 0, '1976-10-23', 1),
(3, 'Daniel Craig', 0, '1968-03-02', 2),
(4, 'Gal Gadot', 1, '1985-04-30', 6),
(5, 'Sam Roxkwell', 0, '1968-11-05', 1),
(6, 'Rebel Wilson ', 0, '1980-03-02', 4),
(7, 'Gina Rodriguez', 1, '1984-06-30', 1),
(8, 'Jennifer Jason Leigh', 1, '1962-02-05', 1),
(9, 'Finn Jones', 0, '1988-03-24', 2),
(10, 'Sebastian Stan', 0, '1982-08-13', 1),
(11, 'Patrick Swayze', 0, '1952-08-18', 1);

--
-- Megkötések a kiírt táblákhoz
--

--
-- Megkötések a táblához `film`
--
ALTER TABLE `film`
  ADD CONSTRAINT `Film_rendezo_id` FOREIGN KEY (`Film_rendezo_id`) REFERENCES `rendezo` (`Rendezo_id`) ON UPDATE CASCADE;

--
-- Megkötések a táblához `filmmufaj`
--
ALTER TABLE `filmmufaj`
  ADD CONSTRAINT `FilmMufaj_id_Film_id` FOREIGN KEY (`FilmMufaj_id_Film_id`) REFERENCES `film` (`Film_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `FilmMufaj_id_Film_mufaj_id` FOREIGN KEY (`FilmMufaj_id_Film_mufaj_id`) REFERENCES `mufaj` (`Mufaj_id`) ON UPDATE CASCADE;

--
-- Megkötések a táblához `rendezes`
--
ALTER TABLE `rendezes`
  ADD CONSTRAINT `rendezes_film_id` FOREIGN KEY (`Rendezes_Film_id`) REFERENCES `film` (`Film_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `rendezes_rendezo_id` FOREIGN KEY (`Rendezes_Rendezo_id`) REFERENCES `rendezo` (`Rendezo_id`) ON UPDATE CASCADE;

--
-- Megkötések a táblához `rendezo`
--
ALTER TABLE `rendezo`
  ADD CONSTRAINT `Rendezo_nemzetiseg` FOREIGN KEY (`Rendezo_nemzetiseg_id`) REFERENCES `nemzetiseg` (`Nemzetiseg_id`) ON UPDATE CASCADE;

--
-- Megkötések a táblához `szereples`
--
ALTER TABLE `szereples`
  ADD CONSTRAINT `Szereples_Film_id` FOREIGN KEY (`Szereples_Film_id`) REFERENCES `film` (`Film_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `Szereples_Szinesz_id` FOREIGN KEY (`Szereples_Szinesz_id`) REFERENCES `szinesz` (`Szinesz_id`) ON UPDATE CASCADE;

--
-- Megkötések a táblához `szinesz`
--
ALTER TABLE `szinesz`
  ADD CONSTRAINT `szinesz_nemzetiseg_id` FOREIGN KEY (`Szinesz_nemzetiseg_id`) REFERENCES `nemzetiseg` (`Nemzetiseg_id`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
