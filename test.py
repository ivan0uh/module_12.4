import logging
import unittest
from runner import Runner

class RunnerTest(unittest.TestCase):
    is_frozen = False

    def test_walk(self):

        try:
            walk_name = Runner('walk_name', -5)
            for i in range(10):
                walk_name.walk()

            self.assertEqual(walk_name.distance, 50)
            logging.info('test_walk выполнен успешно')
        except:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            run_name = Runner(4)
            for i in range(10):
                run_name.run()
            self.assertEqual(run_name.distance, 100)
            logging.info('test_run выполнен успешно')
        except:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    def test_challenge(self):
        challenge_name_1 = Runner("Challenge_name_1")
        challenge_name_2 = Runner("Challenge_name_2")
        for i in range(10):
            challenge_name_1.walk()
            challenge_name_2.run()
        self.assertNotEqual(challenge_name_1.distance, challenge_name_2.distance)




logging.basicConfig(level=logging.INFO, filemode='w', filename="runner_t.log", encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')