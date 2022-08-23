from unittest import TestCase, main

from project.hero import Hero


class HeroTest(TestCase):
    def setUp(self) -> None:
        self.hero = Hero(username="Krali Marko", level=10, health=100, damage=100)
        self.enemy_hero = Hero(username="Kara Ibrahim Besni", level=10, health=100, damage=100)

    def test_hero_constructor(self):
        self.assertEqual("Krali Marko", self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, self.hero.damage)

    def test_enemy_hero_constructor(self):
        self.assertEqual("Kara Ibrahim Besni", self.enemy_hero.username)
        self.assertEqual(10, self.enemy_hero.level)
        self.assertEqual(100, self.enemy_hero.health)
        self.assertEqual(100, self.enemy_hero.damage)

    def test_battle_with_yourself_raises(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        expected = "You cannot fight yourself"
        actual = str(ex.exception)
        self.assertEqual(expected, actual)

    def test_battle_with_zero_health_raises(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)
        expected = "Your health is lower than or equal to 0. You need to rest"
        actual = str(ex.exception)
        self.assertEqual(expected, actual)

    def test_battle_with_negative_health_raises(self):
        self.hero.health = -1
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)
        expected = "Your health is lower than or equal to 0. You need to rest"
        actual = str(ex.exception)
        self.assertEqual(expected, actual)

    def test_battle_with_enemy_zero_health_raises(self):
        self.enemy_hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)
        expected = f"You cannot fight {self.enemy_hero.username}. He needs to rest"
        actual = str(ex.exception)
        self.assertEqual(expected, actual)

    def test_battle_with_enemy_negative_health_raises(self):
        self.enemy_hero.health = -1
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)
        expected = f"You cannot fight {self.enemy_hero.username}. He needs to rest"
        actual = str(ex.exception)
        self.assertEqual(expected, actual)

    def test_battle_you_win_scenario(self):
        self.enemy_hero.damage = 1
        battle_outcome = self.hero.battle(self.enemy_hero)
        self.assertEqual(11, self.hero.level)
        self.assertEqual(95, self.hero.health)
        self.assertEqual(105, self.hero.damage)
        self.assertEqual(-900, self.enemy_hero.health)
        self.assertEqual("You win", battle_outcome)

    def test_battle_you_loose_scenario(self):
        hero = Hero(username="Krali Marko", level=1, health=100, damage=50)
        enemy_hero = Hero(username="Kara Ibrahim Besni", level=1, health=100, damage=50)
        battle_outcome = hero.battle(enemy_hero)
        self.assertEqual(2, enemy_hero.level)
        self.assertEqual(55, enemy_hero.health)
        self.assertEqual(55, enemy_hero.damage)
        self.assertEqual(50, hero.health)
        self.assertEqual("You lose", battle_outcome)

    def test_battle_draw_scenario(self):
        battle_outcome = self.hero.battle(self.enemy_hero)
        self.assertEqual(-900, self.hero.health)
        self.assertEqual(-900, self.enemy_hero.health)
        self.assertEqual("Draw", battle_outcome)

    def test_hero_to_string(self):
        expected = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n"
        actual = str(self.hero)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()