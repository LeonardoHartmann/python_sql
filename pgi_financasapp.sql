-- --------------------------------------------------------
-- Servidor:                     127.0.0.1
-- Versão do servidor:           10.4.27-MariaDB - mariadb.org binary distribution
-- OS do Servidor:               Win64
-- HeidiSQL Versão:              12.4.0.6667
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Copiando estrutura do banco de dados para pgi_financasapp
CREATE DATABASE IF NOT EXISTS `pgi_financasapp` /*!40100 DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci */;
USE `pgi_financasapp`;

-- Copiando estrutura para tabela pgi_financasapp.lancamento
DROP TABLE IF EXISTS `lancamento`;
CREATE TABLE IF NOT EXISTS `lancamento` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo` int(11) NOT NULL,
  `data` date NOT NULL,
  `observacao` varchar(100) DEFAULT NULL,
  `valor` decimal(15,2) NOT NULL DEFAULT 0.00,
  PRIMARY KEY (`id`),
  KEY `FK_LANCAMENTO_TIPO` (`tipo`),
  CONSTRAINT `FK_LANCAMENTO_TIPO` FOREIGN KEY (`tipo`) REFERENCES `tipo` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Copiando dados para a tabela pgi_financasapp.lancamento: ~1 rows (aproximadamente)
INSERT INTO `lancamento` (`id`, `tipo`, `data`, `observacao`, `valor`) VALUES
	(13, 2, '2023-03-10', 'gesdf', 111.00);

-- Copiando estrutura para tabela pgi_financasapp.saldodiario
DROP TABLE IF EXISTS `saldodiario`;
CREATE TABLE IF NOT EXISTS `saldodiario` (
  `data` date NOT NULL,
  `saldo` decimal(15,2) DEFAULT NULL,
  PRIMARY KEY (`data`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Copiando dados para a tabela pgi_financasapp.saldodiario: ~0 rows (aproximadamente)
INSERT INTO `saldodiario` (`data`, `saldo`) VALUES
	('2023-03-10', -111.00);

-- Copiando estrutura para tabela pgi_financasapp.tipo
DROP TABLE IF EXISTS `tipo`;
CREATE TABLE IF NOT EXISTS `tipo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descricao` varchar(50) DEFAULT NULL,
  `tipo` char(1) DEFAULT NULL COMMENT 'E - Entrada / S - Saida',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Copiando dados para a tabela pgi_financasapp.tipo: ~7 rows (aproximadamente)
INSERT INTO `tipo` (`id`, `descricao`, `tipo`) VALUES
	(1, 'salario', 'E'),
	(2, 'coca', 'S'),
	(3, 'teste222', 'S'),
	(6, 'teste 2', 'S'),
	(7, 'teste 2', 'S'),
	(8, 'teste 2', 'S'),
	(9, 'teste', 't'),
	(10, 'teste', 's'),
	(11, 'string', 's'),
	(12, 'string', 's'),
	(13, 'string', 's');

-- Copiando estrutura para trigger pgi_financasapp.lancamento_after_insert
DROP TRIGGER IF EXISTS `lancamento_after_insert`;
SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_ZERO_IN_DATE,NO_ZERO_DATE,NO_ENGINE_SUBSTITUTION';
DELIMITER //
CREATE TRIGGER `lancamento_after_insert` AFTER INSERT ON `lancamento` FOR EACH ROW BEGIN
	DECLARE iExiste INTEGER;
	DECLARE sTipo char(1);

	select count(*) into iExiste
	from saldodiario
	where `data` = new.data;
	
	select tipo into sTipo
	from tipo
	where id = new.tipo;
	
	if (iExiste = 0) then
		if (sTipo = 'E') then
			INSERT INTO saldodiario(`data`, saldo)
			VALUES(NEW.data, new.valor);
		else
			INSERT INTO saldodiario(`data`, saldo)
			VALUES(NEW.data, new.valor * (-1) );
		END if;
	else
		if (sTipo = 'E') THEN
			-- vai somar no saldo
			update saldodiario
			set saldo = saldo + new.valor
			where `data` = new.data;
		ELSE
			-- vai tirar do saldo
			update saldodiario
			set saldo = saldo - new.valor
			where `data` = new.data;
		end if;
	END if;
END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

-- Copiando estrutura para trigger pgi_financasapp.lancamento_AFTER_UPDATE
DROP TRIGGER IF EXISTS `lancamento_AFTER_UPDATE`;
SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_ZERO_IN_DATE,NO_ZERO_DATE,NO_ENGINE_SUBSTITUTION';
DELIMITER //
CREATE TRIGGER `lancamento_AFTER_UPDATE` AFTER UPDATE ON `lancamento` FOR EACH ROW BEGIN
	DECLARE iExiste INTEGER;
	DECLARE sTipo char(1);
	
	select tipo into sTipo
	from tipo
	where id = old.tipo;
	if (sTipo = 'E') THEN
		-- vai somar no saldo
		update saldodiario
		set saldo = saldo - old.valor
		where `data` = old.data;
	ELSE
		-- vai tirar do saldo
		update saldodiario
		set saldo = saldo + old.valor
		where `data` = old.data;
	end if;
	
	select count(*) into iExiste
	from saldodiario
	where `data` = new.data;
	
	select tipo INTO sTipo
	from tipo
	where id = new.tipo;
	
	if (iExiste = 0) then
		if (sTipo = 'E') then
			INSERT INTO saldodiario(`data`, saldo)
			VALUES(NEW.data, new.valor);
		else
			INSERT INTO saldodiario(`data`, saldo)
			VALUES(NEW.data, new.valor * (-1));
		END if;
	else

		
		if (sTipo = 'E') THEN
			-- vai somar no saldo
			update saldodiario
			set saldo = saldo + new.valor
			where `data` = new.data;
		ELSE
			-- vai tirar do saldo
			update saldodiario
			set saldo = saldo - new.valor
			where `data` = new.data;
		end if;
	END if;
END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

-- Copiando estrutura para trigger pgi_financasapp.lancamento_before_delete
DROP TRIGGER IF EXISTS `lancamento_before_delete`;
SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_ZERO_IN_DATE,NO_ZERO_DATE,NO_ENGINE_SUBSTITUTION';
DELIMITER //
CREATE TRIGGER `lancamento_before_delete` BEFORE DELETE ON `lancamento` FOR EACH ROW BEGIN
	DECLARE sTipo char(1);
	
	select tipo into sTipo
	from tipo
	where id = old.tipo;
	
	if (sTipo = 'E') THEN
		-- vai somar no saldo
		update saldodiario
		set saldo = saldo - old.valor
		where `data` = old.data;
	ELSE
		-- vai tirar do saldo
		update saldodiario
		set saldo = saldo + old.valor
		where `data` = old.data;
	end if;
END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
