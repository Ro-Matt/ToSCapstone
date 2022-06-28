import spacy
from spacy.matcher import PhraseMatcher
    
# set up global nlp 
nlp = spacy.load("en_core_web_sm")

class spacyClass:
    # text from TOS
    fullText = None
    # patterns to be nlp'd and matched
    patterns = None 
    # list of index number and text to be filled for matches
    matchedDict = {} 
    # spacy matcher object
    matcher = PhraseMatcher(nlp.vocab, attr="LEMMA")
    """_summary_
    """
    def __init__(self):
        self.patterns = [None]*50 
        self.text = [None]*50 

        self.patterns[0] = [nlp("perpetual"), nlp("irrevocable")]
        # self.matcher.add("OA", self.patterns[0])
        self.patterns[1] = [nlp("you maintain ownership"), nlp("you retain ownership"), nlp(
         "you retain all"), nlp("do not claim ownership"), nlp("you own the"), nlp("do not claim any ownership")]
        # self.matcher.add("OB", self.patterns[1])
        self.patterns[2] = [nlp("you waive any"), nlp("you waive your"), nlp("hereby waive"), nlp("irrevocably waive"), nlp("waive your moral right") ] 
        # self.matcher.add("OC", self.patterns[2])
        self.patterns[3] = [nlp("without any compensation"), nlp("without any payment"), nlp("without any obligation"), nlp("without any restriction") ] 
        # self.matcher.add("OD", self.patterns[3])
        self.patterns[4] = [nlp("without prior notice"), nlp("any time without notice"), nlp("any time for any reason"), nlp("without notice to you")]
        # self.matcher.add("OE", self.patterns[4])
        self.patterns[5] = [nlp("(30) day written notice"), nlp("30 day written notice"), nlp("30 day notice")] 
        # self.matcher.add("OF", self.patterns[5])
        self.patterns[6] = [nlp("infringe"), nlp("copyright infringe")]
        # self.matcher.add("OG", self.patterns[6])
        self.patterns[7] = [nlp("reserve the right to edit"), nlp("remove or edit"), nlp("may edit")]
        # self.matcher.add("OH", self.patterns[7])
        self.patterns[8] = [nlp("at any time without prior notice"), nlp("at any time, without prior notice"), nlp("at its sole discretion")]
        # self.matcher.add("OI", self.patterns[8])
        self.patterns[9] = [nlp("remove, block"), nlp("edit, block"), nlp("refuse to post") ]
        # self.matcher.add("OJ", self.patterns[9])
        self.patterns[10] = [nlp("repeat ingringe"), nlp("repeat copyright infringe")]
        # self.matcher.add("OK", self.patterns[10])
        self.patterns[11] = [nlp("discontinue the service"), nlp("discontinue part of the service"), nlp("discontinue some or all")]
        # self.matcher.add("OL", self.patterns[11])
        self.patterns[12] = [nlp("not re-register"), nlp("previous remove"), nlp("previous disable"), nlp("previous suspend")]
        # self.matcher.add("OM", self.patterns[12])
        self.patterns[13] = [nlp("submit a copyright"), nlp("you believe that your work has been copied")]
        # self.matcher.add("ON", self.patterns[13])
        self.patterns[14] = [nlp("counter-notice"), nlp("counter notice"), nlp("counter-notification")]
        # self.matcher.add("OO", self.patterns[14])
        self.patterns[15] = [nlp("perpetual"), nlp("irrevocable")]
        # self.matcher.add("OP", self.patterns[15])
        self.patterns[16] = [nlp("nonexclusive")]
        # self.matcher.add("OQ", self.patterns[16])
        self.patterns[17] = [nlp("now known or hereafter"), nlp("now known or later")]
        # self.matcher.add("OR", self.patterns[17])
        self.patterns[18] = [nlp("transferable"), nlp("sublicensable"), nlp("sub-licensable")]
        # self.matcher.add("DA", self.patterns[18])
        self.patterns[19] = [nlp("end-to-end encrypt"), nlp("content be encrypt")]
        # self.matcher.add("DB", self.patterns[19])
        self.patterns[20] = [nlp("do not sell")]
        # self.matcher.add("DC", self.patterns[20])
        self.patterns[21] = [nlp("data be aggregate"),nlp("store aggregate"),nlp("de-identify"), nlp("aggregate information"), nlp("aggregate into statistic")]
        # self.matcher.add("DE", self.patterns[21])
        self.patterns[22] = [nlp("we may collect personal data")]# more likely going to have to be manual 
        # self.matcher.add("DF", self.patterns[22])
        self.patterns[23] = [nlp("partner provide information"), nlp("we receive peronal data"), nlp("we receive information")]
        # self.matcher.add("DG", self.patterns[23])
        self.patterns[24] = [nlp("data protection authority"), nlp("data protection office"), nlp("data protection officer"), nlp("data protection supervisor")]
        # self.matcher.add("DH", self.patterns[24])
        self.patterns[25] = []#more than likely going to have to be manual
        # self.matcher.add("DI", self.patterns[25])
        self.patterns[26] = [nlp("collect location information"), nlp("about your location"), nlp("precise location")]
        # self.matcher.add("DJ", self.patterns[26])
        self.patterns[27] = [nlp("use for many different purpose"), nlp("personalize your experience"), nlp("provide advertising")]#manual help
        # self.matcher.add("DK", self.patterns[27])
        self.patterns[28] = [nlp("scan and analyze"), nlp("scan technology"), nlp("review your messages"), nlp("private message")]
        # self.matcher.add("DL", self.patterns[28])
        self.patterns[29] = [nlp("receive certain information"), nlp("receive information"), nlp("other website")]
        # self.matcher.add("0", self.patterns[29])
        self.patterns[30] = [nlp("cookie be not"), nlp("cookie do not"), nlp("do not use cookie")]
        # self.matcher.add("DN", self.patterns[30])
        self.patterns[31] = [nlp("third party cookie"), nlp("partner use"), nlp("third-party advertise"), nlp("third-party service provider"), nlp("Google Analytics")]
        # self.matcher.add("DO", self.patterns[31])
        self.patterns[32] = [nlp("refer page"), nlp("refer source"), nlp("refer web page"), nlp("exit page"), nlp("referral source"), nlp("referall web page"), nlp("referral source") ]
        # self.matcher.add("DP", self.patterns[32])
        self.patterns[33] = [nlp("do not use any cookie or track"), nlp("do not use cookie"), nlp("never collect"), nlp("not be track")]
        # self.matcher.add("DQ", self.patterns[33])
        self.patterns[34] = [nlp("pixel tag"), nlp("Facebook pixel"),nlp ("social media cookie"), nlp("social media feature")]
        # self.matcher.add("DR", self.patterns[34])
        self.patterns[35] = [nlp("refuse cookie"), nlp("reject cookie"), nlp("block cookie"), nlp("delete cookie"), nlp("decline cookie")]
        # self.matcher.add("DS", self.patterns[35])
        self.patterns[36] = [nlp("session cookie"), nlp("session data")]
        # self.matcher.add("DT", self.patterns[36])
        self.patterns[37] = [nlp("web beacon"), nlp("tracking pixel"),nlp("browser fingerprint"), nlp("device fingerpint"), nlp("pixel tag")]
        # self.matcher.add("DU", self.patterns[37])
        self.patterns[38] = [nlp("flash cookie"), nlp("Flash cookie")]
        # self.matcher.add("DV", self.patterns[38])
        self.patterns[39] = [nlp("we do not respond to")]
        # self.matcher.add("DW", self.patterns[39])
        self.patterns[40] = [nlp("enable do not track"), nlp("do not track enable"), nlp("respect your browser")]
        # self.matcher.add("DX", self.patterns[40])
        self.patterns[41] = [nlp("security breach"), nlp("breach of security"), nlp("data breach"), nlp("breach of data")]
        # self.matcher.add("DY", self.patterns[41])
        self.patterns[42] = [nlp("long as is necessary"), nlp("long as necessary"), nlp("retain your personal data"), nlp("retain your data")]
        # self.matcher.add("DZ", self.patterns[42])
        self.patterns[43] = [nlp("do not log your ip"), nlp("do not collect ip"), nlp("do not record your login ip"), nlp("do not record your ip")]
        # self.matcher.add("DDA", self.patterns[43])
        self.patterns[44] = [nlp("collect your IP address"), nlp("include your ip address"), nlp("include ip address"), nlp("such as ip address"), nlp("such as your ip address"), nlp("approximate location")]
        # self.matcher.add("DDB", self.patterns[44])
        self.patterns[45] = [nlp("gps")]#subjective to if device requires precise location
        # self.matcher.add("DDC", self.patterns[45])
        self.patterns[46] = [nlp("biometric"), nlp("fingerprint"), nlp("call recording")]
        # self.matcher.add("DDD", self.patterns[46])
        self.patterns[47] = [nlp("browse history")]
        # self.matcher.add("DDE", self.patterns[47])
        self.patterns[48] = [nlp("right to request"), nlp("request access"), nlp("request deletion"), nlp("delete your information")]
        # self.matcher.add("DDF", self.patterns[48])
        self.patterns[49] = [nlp("copy of your personal data"), nlp("copy of the personal data"), nlp("copy of your personal information"), nlp("copy of this personal information")]
        # self.matcher.add("DDG", self.patterns[49])
    """
    This function is used to fill the text with a file
    """ 
    def fillTextFile(self, file):
        newText = open(file, 'r', encoding = 'utf-8', errors = 'ignore')
        self.fullText = newText.read()
        """
        This function fills the text with a given string
        """
    def fillText(self, t):
        self.fullText = t 

    """
    This is the main function for automatic annotations for a TOS. It uses pre-approved phrases and searches text for matches.
    """
    def phraseMatch(self):
        doc = nlp(self.fullText)
        for i in range(1,50):
            self.matcher.add("ID", self.patterns[i])
            match = self.matcher(doc)
            self.matcher.remove("ID")
            for match_id, start, end in match:
                if i not in self.matchedDict:
                    span = doc[start:end]
                    sents = str(span.sent)
                    self.matchedDict[i] = sents
                break    