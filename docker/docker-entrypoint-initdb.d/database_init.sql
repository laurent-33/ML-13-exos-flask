DROP TABLE IF EXISTS `utilisateurs`;
CREATE TABLE `utilisateurs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(25) NOT NULL,
  `prenom` varchar(25) NOT NULL,
  `sexe` varchar(3) NOT NULL,
  `pseudo` varchar(25) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE (`pseudo`)
);
