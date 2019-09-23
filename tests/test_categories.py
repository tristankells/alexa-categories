import unittest
from Translator import Translator
import Categories



class TestDate(unittest.TestCase):
    def setUp(self):
        self.translator = Translator.Date.Conchita

    def test__skill_launches(self):
        session_variables = {}

        categories = Categories(session_variables)

        categories.

        response = Date(Intents.QUESTION_WHERE_YOU_FROM, session_variables).get_response()

        # Confirm player still in date
        self.assertEqual(slots.AreaEnum.date, response.session_variables.area, )

        # Confirm player has started the right conversation
        self.assertEqual(slots.ConversationEnum.home_place, response.session_variables.conversation)

        # Confirm player gets the correct message
        self.assertEqual(self.translator.question_where_you_from, response.speech_text)

    def test__try_start_conversation__fails_if_they_do_not_ask_a_question(self):
        session_variables = {
            SessionVariables.CONVERSATION: 1000,
            SessionVariables.AREA: slots.AreaEnum.date,
            SessionVariables.DATE: DateEnum.conchita,
            SessionVariables.DATE_BAD_RESPONSE_COUNT: 0
        }

        response = Date(Intents.ANSWER_JOB, session_variables).get_response()

        # Confirm player still in date
        self.assertEqual(slots.AreaEnum.date, response.session_variables.area, )
        # Confirm player not in a conversation
        self.assertEqual(slots.ConversationEnum.nothing, response.session_variables.conversation)
        # Confirm player gets the error message
        self.assertEqual(Translator.Date.crickets + Translator.Date.Error.first_mistake, response.speech_text)
        # Confirm player bad response count has increased
        self.assertEqual(1, response.session_variables.date_bad_response_count)

    def test_date__try_continue_conversation__succeeds_if_they_answer_the_right_question(self):
        session_variables = {
            SessionVariables.CONVERSATION: slots.ConversationEnum.name,
            SessionVariables.AREA: slots.AreaEnum.date,
            SessionVariables.DATE: DateEnum.conchita,
            SessionVariables.DATE_ROUND: 0,
        }

        response = Date(Intents.ANSWER_NAME, session_variables).get_response()

        # Confirm player no longer in conversation in a conversation
        self.assertEqual(slots.ConversationEnum.nothing, response.session_variables.conversation)
        # Confirm player gets the correct answer from their date
        self.assertEqual(Translator.Date.point + self.translator.answer_name, response.speech_text)
        # Confirm the round counter has increased
        self.assertEqual(1, response.session_variables.date_round)

    def test_date__try_continue_conversation__fails_if_they_answer_the_wrong_question(self):
        session_variables = {
            SessionVariables.CONVERSATION: slots.ConversationEnum.name,
            SessionVariables.AREA: slots.AreaEnum.date,
            SessionVariables.DATE: DateEnum.conchita,
            SessionVariables.DATE_ROUND: 0,
        }

        response = Date(Intents.ANSWER_JOB, session_variables).get_response()

        # Confirm player no longer in conversation in a conversation
        self.assertEqual(slots.ConversationEnum.nothing, response.session_variables.conversation)
        # Confirm player gets the correct answer from their date
        self.assertEqual(Translator.Date.crickets + Translator.Date.Error.first_mistake, response.speech_text)

    def test_date__date_finishes_after_the_last_round_right_answer(self):
        session_variables = {
            SessionVariables.CONVERSATION: slots.ConversationEnum.animal,
            SessionVariables.AREA: slots.AreaEnum.date,
            SessionVariables.DATE: DateEnum.conchita,
            SessionVariables.DATE_ROUND: ROUNDS_PER_DATE - 1,
            SessionVariables.DATE_SCORE: 2
        }

        response = Date(Intents.ANSWER_ANIMALS, session_variables).get_response()

        self.assertEqual(slots.ConversationEnum.nothing, response.session_variables.conversation,
                         'Player should no longer be in a conversation')

        self.assertEqual(0, response.session_variables.date_round, 'Date round should have been reset 0')

        self.assertEqual(Translator.Date.point + self.translator.answer_animals + Translator.Date.finish.format('3'),
                         response.speech_text,
                         'Player should get an answer to their question followed by the finishing date dialog')

        self.assertEqual(0, response.session_variables.date_score, 'The date score should be reset to 0')

        self.assertNotEqual(DateEnum.conchita, response.session_variables.date,
                            'They should not be on a date with the same person')

    def test_date__date_finishes_after_the_last_round_wrong_answer(self):
        session_variables = {
            SessionVariables.CONVERSATION: slots.ConversationEnum.name,
            SessionVariables.AREA: slots.AreaEnum.date,
            SessionVariables.DATE: DateEnum.conchita,
            SessionVariables.DATE_ROUND: ROUNDS_PER_DATE - 1,
            SessionVariables.DATE_SCORE: 2,
            SessionVariables.DATE_BAD_RESPONSE_COUNT: 1
        }

        response = Date(Intents.ANSWER_ANIMALS, session_variables).get_response()

        self.assertEqual(slots.ConversationEnum.nothing, response.session_variables.conversation,
                         'Player should no longer be in a conversation')

        self.assertEqual(0, response.session_variables.date_round, 'Date round should have been reset 0')

        self.assertEqual(
            Translator.Date.crickets + Translator.Date.Error.second_mistake + Translator.Date.finish.format('2'),
            response.speech_text,
            'Player should get an error message followed by the finishing date dialog')

        self.assertEqual(0, response.session_variables.date_score, 'The date score should be reset to 0')

        self.assertNotEqual(DateEnum.conchita, response.session_variables.date,
                            'They should not be on a date with the same person')

    def test_date__date_finishes_after_the_three_bad_response(self):
        session_variables = {
            SessionVariables.CONVERSATION: slots.ConversationEnum.nothing,
            SessionVariables.AREA: slots.AreaEnum.date,
            SessionVariables.DATE: DateEnum.conchita,
            SessionVariables.DATE_ROUND: 1,
            SessionVariables.DATE_SCORE: 0,
            SessionVariables.DATE_BAD_RESPONSE_COUNT: 2
        }

        response = Date(Intents.ANSWER_ANIMALS, session_variables).get_response()

        self.assertEqual(slots.ConversationEnum.nothing, response.session_variables.conversation,
                         'Player should no longer be in a conversation')

        self.assertEqual(0, response.session_variables.date_round, 'Date round should have been reset 0')

        self.assertEqual(
            Translator.Date.crickets + Translator.Date.Error.third_mistake + Translator.Date.finish.format('0'),
            response.speech_text,
            'Player should get the final error message + the date over message')

        self.assertEqual(0, response.session_variables.date_score, 'The date score should be reset to 0')

        self.assertNotEqual(DateEnum.conchita, response.session_variables.date,
                            'They should not be on a date with the same person')

    def test_date__date_repeats_response_if_asked(self):
        session_variables = {
            SessionVariables.CONVERSATION: slots.ConversationEnum.colour,
            SessionVariables.AREA: slots.AreaEnum.date,
            SessionVariables.DATE: DateEnum.conchita,
            SessionVariables.DATE_ROUND: 1,
            SessionVariables.DATE_SCORE: 0,
            SessionVariables.DATE_BAD_RESPONSE_COUNT: 2,
            SessionVariables.PREVIOUS_INTENT : Intents.QUESTION_COLOUR
        }

        response = Date(Intents.REPEAT, session_variables).get_response()

        self.assertEqual(
            self.translator.question_colour, response.speech_text, 'Player should hear the correct response, repeated')




if __name__ == '__main__':
    unittest.main()