from tokenizer import tokenize, TOK

class IcelandicTokeniser(SUtteranceProcessor):
    '''
    A very crude tokeniser, which:

    1. splits text with a regular expression specified
    in config file, which defaults to whitespace. Note that whether spaces etc. are
    treated as tokens or not depends on use of brackets in the regex -- cf. (\s+) and \s+

    2. optionally

    3. classifies tokens on the basis of regex

    4. optionally add safetext representation
    '''
    def __init__(self, processor_name='icelandic_tokeniser', target_nodes = '//utt', split_attribute = 'text', \
                child_node_type = 'token', add_terminal_tokens=True, \
                add_token_classes = True, \
                default_class = 'word', class_attribute='token_class',
                add_safetext = True,
                safetext_attribute = 'safetext', \
                class_patterns = [('space', '\A\s+\Z'), ('punctuation', '\A[\.\,\;\!\?\s]+\Z')],
                lowercase_safetext = True):


        self.processor_name = processor_name

        self.target_nodes = target_nodes
        self.split_attribute = split_attribute
        self.child_node_type = child_node_type
        self.add_terminal_tokens = add_terminal_tokens
        self.default_class = default_class
        self.class_attribute = class_attribute
        self.add_token_classes = add_token_classes
        self.class_patterns = [(name, new_regex.compile(patt)) for (name, patt) in class_patterns]

        self.add_safetext = add_safetext
        self.safetext_attribute = safetext_attribute
        self.lowercase_safetext = lowercase_safetext

        super(IcelandicTokeniser, self).__init__()


    def process_utterance(self, utt):

        #print 'target nodes: %s'%(utt.xpath(self.target_nodes))
        for node in utt.xpath(self.target_nodes):
            assert node.has_attribute(self.split_attribute)
            to_split = node.get(self.split_attribute)

            child_chunks = self.splitting_function(to_split)

            for chunk in child_chunks:
                #print '=='
                #print chunk
                child = Element(self.child_node_type)
                child.set(self.split_attribute, chunk)
                if self.add_token_classes:
                    token_class = self.classify_token(chunk)
                    #print token_class
                    child.set(self.class_attribute, token_class)

                if self.add_safetext:
                    token_safetext = self.safetext_token(chunk)
                    child.set(self.safetext_attribute, token_safetext)

                node.add_child(child)

    def classify_token(self, token):

        ## Special handling of terminal token:
        if token == c.TERMINAL:
            return c.TERMINAL
        for (item_class, pattern) in self.class_patterns:
            if pattern.match(token):
                return item_class
        return self.default_class

    def safetext_token(self, instring):
        ## Special handling of terminal token:
        if instring == c.TERMINAL:
            return c.TERMINAL
        else:
            if self.lowercase_safetext == 'True':
                return naive_util.safetext(instring.lower())
            else:
                return naive_util.safetext(instring)

    def splitting_function(self, instring):
        tokens = tokenize(instring)
        tokens = [w for t in tokens if t.txt is not None and t.txt != '' for w in t.txt.split()]
        if self.add_terminal_tokens:
            tokens = [c.TERMINAL] + tokens + [c.TERMINAL]
        return tokens

    def do_training(self, speech_corpus, text_corpus):
        print "IcelandicTokeniser requires no training"