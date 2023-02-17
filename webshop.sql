-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Gép: 127.0.0.1
-- Létrehozás ideje: 2023. Feb 17. 23:02
-- Kiszolgáló verziója: 10.4.20-MariaDB
-- PHP verzió: 8.0.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Adatbázis: `webshop`
--

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `categorys`
--

CREATE TABLE `categorys` (
  `id` int(11) NOT NULL,
  `name` varchar(50) COLLATE utf8mb4_hungarian_ci NOT NULL,
  `company_ids` varchar(100) COLLATE utf8mb4_hungarian_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_hungarian_ci;

--
-- A tábla adatainak kiíratása `categorys`
--

INSERT INTO `categorys` (`id`, `name`, `company_ids`) VALUES
(2, 'Élelmiszer', '1,3'),
(3, 'Bútor', '1'),
(4, 'Konyhai eszköz', '1'),
(5, 'Fürdőszobai kellékek', '1'),
(6, 'Ruha', '1'),
(7, 'Sport eszköz', '1'),
(8, 'Művészeti kellék', '1'),
(9, 'Elektromos berendezés', '1'),
(12, 'Fagylalt', '1,3'),
(16, 'Iskolai eszköz', '1');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `companies`
--

CREATE TABLE `companies` (
  `id` int(11) NOT NULL,
  `nav_name` varchar(255) COLLATE utf8mb4_hungarian_ci NOT NULL,
  `short_nav_name` varchar(255) COLLATE utf8mb4_hungarian_ci NOT NULL,
  `phone` varchar(255) COLLATE utf8mb4_hungarian_ci NOT NULL,
  `email` varchar(255) COLLATE utf8mb4_hungarian_ci NOT NULL,
  `city` varchar(255) COLLATE utf8mb4_hungarian_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_hungarian_ci;

--
-- A tábla adatainak kiíratása `companies`
--

INSERT INTO `companies` (`id`, `nav_name`, `short_nav_name`, `phone`, `email`, `city`) VALUES
(1, 'Balogh Fogd étel ház KFT', 'BFEH Kft.', '0630-343-4444', 'norbi@gmail.com', 'Kisvárda'),
(3, 'Étel bár Kft.', 'EB Kft.', '06304445555', 'eb@eb.com', 'Eb vár'),
(4, 'Nem tudom mi legyen a neve Kft.', 'NMML Kft.', '06-30-444-5555', 'nmml@nem.com', 'Pest út 10');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `logging`
--

CREATE TABLE `logging` (
  `id` int(11) NOT NULL,
  `description` text COLLATE utf8mb4_hungarian_ci NOT NULL,
  `period` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_hungarian_ci;

--
-- A tábla adatainak kiíratása `logging`
--

INSERT INTO `logging` (`id`, `description`, `period`) VALUES
(5, 'gdfgdfg dfgddf', '2022-05-23 19:08:00'),
(6, 'gdfgdfg dfgddf teset', '2022-06-05 19:08:00'),
(7, 'dgdfdg df gdfg dgdf dg df gdfg dgdfdg df gdfg dgd\n\n', '2022-08-04 20:20:00'),
(10, 'teSTET', '2022-04-06 20:49:00'),
(11, 'TEST', '2022-04-04 20:50:00');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `permissions`
--

CREATE TABLE `permissions` (
  `id` int(11) NOT NULL,
  `page` varchar(25) COLLATE utf8mb4_hungarian_ci NOT NULL,
  `description` varchar(255) COLLATE utf8mb4_hungarian_ci NOT NULL,
  `role_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_hungarian_ci;

--
-- A tábla adatainak kiíratása `permissions`
--

INSERT INTO `permissions` (`id`, `page`, `description`, `role_id`) VALUES
(1, 'products', 'view,update,delete,create', 1),
(2, 'categories', 'view,create,update,delete', 1),
(3, 'partners', 'view,create,update,delete', 1),
(4, 'logging', 'view,create,update,delete', 1),
(5, 'options', 'view,create,update,delete', 1);

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `products`
--

CREATE TABLE `products` (
  `id` int(11) NOT NULL,
  `product_id` varchar(255) COLLATE utf8mb4_hungarian_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_hungarian_ci NOT NULL,
  `category_id` int(11) NOT NULL,
  `company_id` int(11) NOT NULL,
  `unit` varchar(50) COLLATE utf8mb4_hungarian_ci NOT NULL,
  `price` int(11) NOT NULL,
  `guarantee` date NOT NULL,
  `retrieved_from` datetime DEFAULT NULL,
  `accepted` datetime DEFAULT NULL,
  `created` datetime NOT NULL DEFAULT current_timestamp(),
  `deleted` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_hungarian_ci;

--
-- A tábla adatainak kiíratása `products`
--

INSERT INTO `products` (`id`, `product_id`, `name`, `category_id`, `company_id`, `unit`, `price`, `guarantee`, `retrieved_from`, `accepted`, `created`, `deleted`) VALUES
(1, 'TTFSF-s', 'sajt', 2, 1, 'kg', 250, '2022-01-12', NULL, '2022-05-15 19:58:58', '2022-01-20 10:38:35', NULL),
(2, 'TTFSF-s', 'test', 4, 1, 'db', 1500, '2022-01-01', '2022-04-25 19:19:58', '2022-04-25 19:19:55', '2022-01-20 11:13:31', NULL),
(4, 'BASTNF-Afsdf', 'sajt', 2, 1, 'kg', 1500, '2022-01-12', NULL, '0000-00-00 00:00:00', '2022-01-20 20:33:30', NULL),
(14, 'KK-r5hdt4', 'Bor', 2, 1, 'L', 15000, '2022-01-27', '2022-03-17 18:45:27', NULL, '2022-01-26 18:48:59', NULL);

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `roles`
--

CREATE TABLE `roles` (
  `id` int(11) NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_hungarian_ci NOT NULL,
  `color` varchar(255) COLLATE utf8mb4_hungarian_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_hungarian_ci;

--
-- A tábla adatainak kiíratása `roles`
--

INSERT INTO `roles` (`id`, `name`, `color`) VALUES
(1, 'admin', '#02dbf7'),
(2, 'jegyző', '#faab00');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `status`
--

CREATE TABLE `status` (
  `id` int(11) NOT NULL,
  `name` varchar(50) COLLATE utf8mb4_hungarian_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_hungarian_ci;

--
-- A tábla adatainak kiíratása `status`
--

INSERT INTO `status` (`id`, `name`) VALUES
(1, 'létrehozva'),
(2, 'elfogadva'),
(3, 'lejárt'),
(4, 'visszaküldve');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(255) COLLATE utf8mb4_hungarian_ci DEFAULT NULL,
  `email` varchar(255) COLLATE utf8mb4_hungarian_ci DEFAULT NULL,
  `password` varchar(255) COLLATE utf8mb4_hungarian_ci NOT NULL,
  `phone` varchar(255) COLLATE utf8mb4_hungarian_ci NOT NULL,
  `role_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_hungarian_ci;

--
-- A tábla adatainak kiíratása `users`
--

INSERT INTO `users` (`id`, `username`, `email`, `password`, `phone`, `role_id`) VALUES
(1, 'norbert', 'norbert@gmail.com', '$2b$12$zUoZr0L5HBRrb3dHdbV3IuCRSD9lq99t94Dw1GEHzSihIECC2G4Be', '06-30-444-4444', 1),
(2, 'Miss titkar', 'titkar@tit.com', '$2b$12$V3zjM3nNYMWKxIi.x8rV5u2IdJUp12sFpXavdvUJV6AzbXoFBqrva', '06-30-444-4444', 2);

--
-- Indexek a kiírt táblákhoz
--

--
-- A tábla indexei `categorys`
--
ALTER TABLE `categorys`
  ADD PRIMARY KEY (`id`);

--
-- A tábla indexei `companies`
--
ALTER TABLE `companies`
  ADD PRIMARY KEY (`id`);

--
-- A tábla indexei `logging`
--
ALTER TABLE `logging`
  ADD PRIMARY KEY (`id`);

--
-- A tábla indexei `permissions`
--
ALTER TABLE `permissions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `roleId` (`role_id`);

--
-- A tábla indexei `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`id`);

--
-- A tábla indexei `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`);

--
-- A tábla indexei `status`
--
ALTER TABLE `status`
  ADD PRIMARY KEY (`id`);

--
-- A tábla indexei `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ix_users_id` (`id`);

--
-- A kiírt táblák AUTO_INCREMENT értéke
--

--
-- AUTO_INCREMENT a táblához `categorys`
--
ALTER TABLE `categorys`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT a táblához `companies`
--
ALTER TABLE `companies`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT a táblához `logging`
--
ALTER TABLE `logging`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT a táblához `permissions`
--
ALTER TABLE `permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT a táblához `products`
--
ALTER TABLE `products`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT a táblához `roles`
--
ALTER TABLE `roles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT a táblához `status`
--
ALTER TABLE `status`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT a táblához `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28792;

--
-- Megkötések a kiírt táblákhoz
--

--
-- Megkötések a táblához `permissions`
--
ALTER TABLE `permissions`
  ADD CONSTRAINT `roleId` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
