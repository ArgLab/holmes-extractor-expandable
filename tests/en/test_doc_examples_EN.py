import os
import unittest
import holmes_extractor as holmes

script_directory = os.path.dirname(os.path.realpath(__file__))
ontology = holmes.Ontology(
    os.sep.join((script_directory, "blog.owl")))
holmes_manager = holmes.Manager(model="en_core_web_trf", number_of_workers=1, ontology=ontology)
holmes_manager.register_search_phrase("A big dog chases a cat")
holmes_manager.register_search_phrase("An ENTITYPERSON goes into town")
holmes_manager.register_search_phrase("A company gives permission to publish something")
holmes_manager.register_search_phrase("An ENTITYPERSON visits an ENTITYGPE")
holmes_manager.register_search_phrase("An ENTITYORG takes over an ENTITYORG")



class EnglishDocumentationExamplesTest(unittest.TestCase):

    positive_examples = (
        "A big dog chased a cat",
        "The big dog would not stop chasing the cat",
        "The big dog who was tired chased the cat",
        "The cat was chased by the big dog",
        "The cat always used to be chased by the big dog",
        "The big dog was going to chase the cat",
        "The big dog decided to chase the cat",
        "The cat was afraid of being chased by the big dog",
        "I saw a cat-chasing big dog",
        "The cat the big dog chased was scared",
        "The big dog chasing the cat was a problem",
        "There was a big dog that was chasing a cat",
        "The cat chase by the big dog",
        "There was a big dog and it was chasing a cat.",
        "I saw a big dog. My cat was afraid of being chased by the dog.",
        "There was a big dog. His name was Fido. He was chasing my cat.",
        "A dog appeared. It was chasing a cat. It was very big.",
        "The cat sneaked back into our lounge because a big dog had been chasing her.",
        "Our big dog was excited because he had been chasing a cat.",
    )

    def test_positive_examples(self):
        for positive_example in self.positive_examples:
            with self.subTest():
                assert len(holmes_manager.match(document_text=positive_example)) == 1

    negative_examples = (
        "The dog chased a big cat",
        "The big dog and the cat chased about",
        "The big dog chased a mouse but the cat was tired",
        "The big dog always used to be chased by the cat",
        "The big dog the cat chased was scared",
        "Our big dog was upset because he had been chased by a cat.",
        "The dog chase of the big cat",
    )

    def test_negative_examples(self):
        for negative_example in self.negative_examples:
            with self.subTest():
                assert len(holmes_manager.match(document_text=negative_example)) == 0

    def test_complex_example(self):
        matches = holmes_manager.match(
            document_text="I met Richard Hudson and John Doe last week. They didn't want to go into town."
        )
        self.assertEqual(
            matches,
            [
                {
                    "search_phrase_label": "An ENTITYPERSON goes into town",
                    "search_phrase_text": "An ENTITYPERSON goes into town",
                    "document": "",
                    "index_within_document": 15,
                    "sentences_within_document": "I met Richard Hudson and John Doe last week. They didn't want to go into town.",
                    "negated": True,
                    "uncertain": True,
                    "involves_coreference": True,
                    "overall_similarity_measure": 1.0,
                    "word_matches": [
                        {
                            "search_phrase_token_index": 1,
                            "search_phrase_word": "ENTITYPERSON",
                            "document_token_index": 3,
                            "first_document_token_index": 2,
                            "last_document_token_index": 3,
                            "structurally_matched_document_token_index": 10,
                            "document_subword_index": None,
                            "document_subword_containing_token_index": None,
                            "document_word": "richard hudson",
                            "document_phrase": "Richard Hudson",
                            "match_type": "entity",
                            "negated": False,
                            "uncertain": True,
                            "similarity_measure": 1.0,
                            "involves_coreference": True,
                            "extracted_word": "richard hudson",
                            "depth": 0,
                            "explanation": "Has an entity label matching ENTITYPERSON.",
                        },
                        {
                            "search_phrase_token_index": 2,
                            "search_phrase_word": "go",
                            "document_token_index": 15,
                            "first_document_token_index": 15,
                            "last_document_token_index": 15,
                            "structurally_matched_document_token_index": 15,
                            "document_subword_index": None,
                            "document_subword_containing_token_index": None,
                            "document_word": "go",
                            "document_phrase": "go",
                            "match_type": "direct",
                            "negated": True,
                            "uncertain": False,
                            "similarity_measure": 1.0,
                            "involves_coreference": False,
                            "extracted_word": "go",
                            "depth": 0,
                            "explanation": "Matches GO directly.",
                        },
                        {
                            "search_phrase_token_index": 3,
                            "search_phrase_word": "into",
                            "document_token_index": 16,
                            "first_document_token_index": 16,
                            "last_document_token_index": 16,
                            "structurally_matched_document_token_index": 16,
                            "document_subword_index": None,
                            "document_subword_containing_token_index": None,
                            "document_word": "into",
                            "document_phrase": "into",
                            "match_type": "direct",
                            "negated": True,
                            "uncertain": False,
                            "similarity_measure": 1.0,
                            "involves_coreference": False,
                            "extracted_word": "into",
                            "depth": 0,
                            "explanation": "Matches INTO directly.",
                        },
                        {
                            "search_phrase_token_index": 4,
                            "search_phrase_word": "town",
                            "document_token_index": 17,
                            "first_document_token_index": 17,
                            "last_document_token_index": 17,
                            "structurally_matched_document_token_index": 17,
                            "document_subword_index": None,
                            "document_subword_containing_token_index": None,
                            "document_word": "town",
                            "document_phrase": "town",
                            "match_type": "direct",
                            "negated": True,
                            "uncertain": False,
                            "similarity_measure": 1.0,
                            "involves_coreference": False,
                            "extracted_word": "town",
                            "depth": 0,
                            "explanation": "Matches TOWN directly.",
                        },
                    ],
                },
                {
                    "search_phrase_label": "An ENTITYPERSON goes into town",
                    "search_phrase_text": "An ENTITYPERSON goes into town",
                    "document": "",
                    "index_within_document": 15,
                    "sentences_within_document": "I met Richard Hudson and John Doe last week. They didn't want to go into town.",
                    "negated": True,
                    "uncertain": True,
                    "involves_coreference": True,
                    "overall_similarity_measure": 1.0,
                    "word_matches": [
                        {
                            "search_phrase_token_index": 1,
                            "search_phrase_word": "ENTITYPERSON",
                            "document_token_index": 6,
                            "first_document_token_index": 5,
                            "last_document_token_index": 6,
                            "structurally_matched_document_token_index": 10,
                            "document_subword_index": None,
                            "document_subword_containing_token_index": None,
                            "document_word": "john doe",
                            "document_phrase": "John Doe",
                            "match_type": "entity",
                            "negated": False,
                            "uncertain": True,
                            "similarity_measure": 1.0,
                            "involves_coreference": True,
                            "extracted_word": "john doe",
                            "depth": 0,
                            "explanation": "Has an entity label matching ENTITYPERSON.",
                        },
                        {
                            "search_phrase_token_index": 2,
                            "search_phrase_word": "go",
                            "document_token_index": 15,
                            "first_document_token_index": 15,
                            "last_document_token_index": 15,
                            "structurally_matched_document_token_index": 15,
                            "document_subword_index": None,
                            "document_subword_containing_token_index": None,
                            "document_word": "go",
                            "document_phrase": "go",
                            "match_type": "direct",
                            "negated": True,
                            "uncertain": False,
                            "similarity_measure": 1.0,
                            "involves_coreference": False,
                            "extracted_word": "go",
                            "depth": 0,
                            "explanation": "Matches GO directly.",
                        },
                        {
                            "search_phrase_token_index": 3,
                            "search_phrase_word": "into",
                            "document_token_index": 16,
                            "first_document_token_index": 16,
                            "last_document_token_index": 16,
                            "structurally_matched_document_token_index": 16,
                            "document_subword_index": None,
                            "document_subword_containing_token_index": None,
                            "document_word": "into",
                            "document_phrase": "into",
                            "match_type": "direct",
                            "negated": True,
                            "uncertain": False,
                            "similarity_measure": 1.0,
                            "involves_coreference": False,
                            "extracted_word": "into",
                            "depth": 0,
                            "explanation": "Matches INTO directly.",
                        },
                        {
                            "search_phrase_token_index": 4,
                            "search_phrase_word": "town",
                            "document_token_index": 17,
                            "first_document_token_index": 17,
                            "last_document_token_index": 17,
                            "structurally_matched_document_token_index": 17,
                            "document_subword_index": None,
                            "document_subword_containing_token_index": None,
                            "document_word": "town",
                            "document_phrase": "town",
                            "match_type": "direct",
                            "negated": True,
                            "uncertain": False,
                            "similarity_measure": 1.0,
                            "involves_coreference": False,
                            "extracted_word": "town",
                            "depth": 0,
                            "explanation": "Matches TOWN directly.",
                        },
                    ],
                },
            ],
        )

    def test_extracted_word_example(self):
        matches = holmes_manager.match(
            document_text="We discussed AstraZeneca. The company had given us permission to publish this library under the MIT license."
        )
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0]["word_matches"][0]["extracted_word"], "astrazeneca")


    def test_blog_example_1(self):
        matches = holmes_manager.match(
            document_text="Richard Hudson visited Berlin"
        )
        self.assertEqual(len(matches), 1)

    def test_blog_example_2(self):
        holmes_manager.remove_all_documents()        
        holmes_manager.parse_and_register_document("Royal Bank of Scotland announces it intends to acquire Brewin Dolphin", "1")
        holmes_manager.parse_and_register_document("Chipmaker MaxLinear Inc announced on Thursday it will buy Silicon Motion Technology Corp for nearly $4 billion.", "2")
        holmes_manager.parse_and_register_document("Last month, cybersecurity company Mandiant was purchased by Alphabet", "3")
        holmes_manager.parse_and_register_document("The Datto takeover by the company Kaseya", "4")
        matches = holmes_manager.match()
        self.assertEqual(len(matches), 4)
        self.assertEqual([match['word_matches'][0]['document_phrase'] for match in matches], ['Royal Bank', 'Chipmaker MaxLinear Inc', 'Alphabet', 'Kaseya'])
        self.assertEqual([match['word_matches'][2]['document_phrase'] for match in matches], ['Brewin Dolphin', 'Silicon Motion Technology Corp', 'cybersecurity company Mandiant', 'Datto'])

    def test_blog_example_3(self):
        holmes_manager.remove_all_documents()
        holmes_manager.parse_and_register_document("The dog was thinking about whether he wanted to chase the neighbourhood cat.", "1")
        holmes_manager.parse_and_register_document("The cat kept chasing around and was hoping she wouldn't see a dog anytime soon.", "2")
        holmes_manager.parse_and_register_document("The children discussed dogs, cats and chasing", "3")
        topic_matches = holmes_manager.topic_match_documents_against("Increasingly, his life's work appeared to revolve around watching dogs chasing cats.")
        self.assertEqual(len(topic_matches), 3)
        self.assertEqual(topic_matches[0]['document_label'], '1')
        self.assertTrue(topic_matches[0]['score'] > topic_matches[1]['score'] * 2)
