from random import shuffle
from random import choice

score= 0
lvl= "easy"
times= 0
welcomeshown= False
started= False
activeword= ""
lives= 5
commands= ["S","s","X","x","R","r","V","v"]


def welcome():
  print("Welcome to the word guessing game")
  print("Guess the right word from the jumbled letters")
  print("Press 'S' to start, 'X' to exit, 'R' to reset and 'V' to view score")
  print("You have ",lives," lives. Good luck!")
  global welcomeshown
  welcomeshown = True

def reset():
  global times, welcomeshown, started, lvl, activeword, score
  times= 0
  score= 0
  welcomeshown= False
  started= False
  lvl= "easy"
  activeword= ""

level= {
  "easy": {
    "value": 1,
    "minWordCount": 3,
    "maxWordCount": 4,
    "words": ["ABLE", "ACID", "ACTS", "ADD", "ADDS", "AGES", "AGO", "AIM", "ALSO", "AND", "ANT", "ANY", "APE", "APPS", "ARE", "AREA", "ARMS", "ARMY", "ARTS", "ASK", "ATE", "AUTO", "AWAY", "AWE", "BABY", "BACK", "BAD", "BAG", "BAGS", "BALL", "BAN", "BAND", "BANK", "BAR", "BARS", "BASE", "BAT", "BAY", "BEAT", "BEE", "BEEN", "BEER", "BEG", "BELT", "BEST", "BET", "BID", "BIG", "BIKE", "BILL", "BIRD", "BIT", "BLOG", "BLUE", "BOAT", "BODY", "BONE", "BOOK", "BORN", "BOSS", "BOTH", "BOWL", "BOY", "BOYS", "BUG", "BUN", "BUS", "BUSY", "BUT", "BUY", "CAKE", "CALL", "CAME", "CAMP", "CAN", "CAR", "CARD", "CARE", "CARS", "CASE", "CASH", "CAST", "CAT", "CATS", "CELL", "CENT", "CITY", "CLUB", "CODE", "COLD", "COME", "COOK", "COOL", "COPY", "CORE", "COST", "COW", "CREW", "CUP", "CUT", "CUTE", "DARK", "DATA", "DATE", "DAY", "DAYS", "DEAD", "DEAL", "DEBT", "DECK", "DEEP", "DESK", "DID DIE", "DIED", "DIET", "DIG", "DIP", "DISH", "DOES", "DOG", "DOGS", "DONE", "DOOR", "DOSE", "DOT", "DOWN", "DRAW", "DROP", "DRUG", "DRY", "DUAL", "DUG", "DUST", "DUTY", "EACH", "EAR", "EARN", "EASE", "EAST", "EASY", "EAT", "EDGE", "EDIT", "EEL", "EGGS", "ELSE", "END", "ENDS", "ERA", "EVEN", "EVER", "EXAM", "EYES", "FACE", "FACT", "FAIL", "FAIR", "FALL", "FAN", "FANS", "FAR", "FARM", "FAST", "FAT", "FEAR", "FEED", "FEEL", "FEES", "FEET", "FELL", "FELT", "FEW", "FILE", "FILL", "FILM", "FIND", "FINE", "FIRE", "FIRM", "FISH", "FIT", "FITS", "FIVE", "FIX", "FLAG", "FLAT", "FLY", "FOG", "FOX", "FRY", "FUN", "FUR", "GAL", "GAP", "GAS", "GAY", "GEM", "GET", "GIG", "GIN", "GOD", "GOT", "GUM", "GUN", "GUT", "GUY", "GYM", "HAD", "HAM", "HAS", "HAT", "HEN", "HER", "HEX", "HEY", "HIM", "HIP", "HIS", "HIT", "HOP", "HOT", "HOW", "HUE", "HUG", "HUM", "HUT", "ICE", "ICY", "ILL", "IRK", "JAB", "JAM", "JAR", "JAW", "JET", "JEW", "JIG", "JOB", "JOG", "JOT", "KEY", "KID", "KIT", "LAP", "LAW", "LAY", "LEG", "LET", "LIE", "LIP", "LOG", "LOW", "MAD", "MAN", "MAP", "MAY", "MEN", "MET", "MIX", "MOB", "MOP", "MOW", "NAG", "NAP", "NET", "NEW", "NIP", "NOD", "NOT", "NOW NUT", "ODD", "OFF", "OIL", "OLD", "ONE", "OUR", "OUT", "OWE", "OWN", "PAT", "PAW", "PEE", "PET", "PIE", "PIG", "PIN", "POT", "PRY", "PUN", "PUT", "RAG", "RAN", "RAY", "RIP", "ROB", "ROT", "ROW", "RUG RUN", "SAD", "SAG", "SAT", "SAW", "SAY", "SEA", "SEE", "SET", "SEW", "SHE", "SHY", "SIP", "SIT", "SIX", "SKY", "SLY", "SON", "SPY", "SUN", "TAG", "TAP", "TAR", "TEN", "TIE", "TIP", "TOO", "TOP", "TOY", "TRY", "TUG", "TWO", "USE", "VAN", "VET", "VEX", "VOW", "WAG", "WAR", "WAS", "WAY", "WET", "WHO", "WHY", "WIG", "YES", "YET", "YIP", "YOU", "ZIP", "ZIT", "ZOO"]
  },
  "medium": {
    "value": 2,
    "minWordCount": 4,
    "maxWordCount": 5,
    "words": ["ABOUT", "ABOVE", "ABUSE", "ADDED", "ADULT", "AFTER", "AGAIN", "AGENT", "AGREE", "AHEAD", "ALBUM", "ALIVE", "ALLOW", "ALONE", "ALONG", "AMONG", "ANGLE", "APART", "APPLE", "APPLY", "AREAS", "ARRAY", "ASIDE", "ASKED", "ASSET", "AUDIO", "AVOID", "AWARD", "AWARE", "BANKS", "BASED", "BASIC", "BASIS", "BEACH", "BEGAN", "BEGIN", "BEING", "BELOW", "BIBLE", "BILLS", "BIRDS", "BIRTH", "BLACK", "BLADE", "BLOCK", "BLOOD", "BOARD", "BONUS", "BOOKS", "BOXES", "BRAIN", "BRAND", "BREAD", "BREAK", "BRIEF", "BRING", "BROAD", "BROKE", "BROWN", "BUILD", "BUILT", "BUNCH", "CABLE", "CALLS", "CARDS", "CARRY", "CASES", "CATCH", "CAUSE", "CELLS", "CHAIN", "CHAIR", "CHART", "CHEAP", "CHECK", "CHEST", "CHIEF", "CHILD", "CHOSE", "CIVIL", "CLAIM", "CLASS", "CLEAN", "CLEAR", "CLICK", "CLOSE", "CLOUD", "CLUBS", "COACH", "COAST", "CODES", "COLOR", "COMES", "COSTS", "COULD", "COUNT", "COURT", "COVER", "CRAFT", "CRAZY", "CREAM", "CRIME", "CROSS", "CROWD", "CROWN", "CYCLE", "DAILY", "DANCE", "DATES", "DEATH", "DEPTH", "DOING", "DOORS", "DOUBT", "DRAFT", "DRAWN", "DREAM", "DRESS", "DRINK", "DRIVE", "DRUGS", "EARLY", "EARTH", "EIGHT", "EMAIL", "EMPTY", "ENDED", "ENEMY", "ENJOY", "ENTER", "ENTRY", "EQUAL", "ERROR", "EVENT", "EVERY", "EXACT", "EXIST", "EXTRA", "FACTS", "FAITH", "FEELS", "FEWER", "FIELD", "FIFTH", "FIGHT", "FILED", "FILES"]
  },
  "hard": {
    "value": 3,
    "minWordCount": 5,
    "maxWordCount": 10,
    "words": ["ABROAD", "ACCEPT", "ACCESS", "ACROSS", "ACTING", "ACTION", "ACTIVE", "ACTUAL", "ADVICE", "ADVISE", "AFFECT", "AFFORD", "AFRAID", "AGENCY", "AGENDA", "ALMOST", "ALWAYS", "AMOUNT", "ANIMAL", "ANNUAL", "ANSWER", "ANYONE", "ANYWAY", "APPEAL", "APPEAR", "AROUND", "ARRIVE", "ARTIST", "ASPECT", "ASSESS", "ASSIST", "ASSUME", "ATTACK", "ATTEND", "AUGUST", "AUTHOR", "AVENUE", "BACKED", "BARELY", "BATTLE", "BEAUTY", "BECAME", "BECOME", "BEFORE", "BEHALF", "BEHIND", "BELIEF", "BELONG", "BERLIN", "BETTER", "BEYOND", "BISHOP", "BORDER", "BOTTLE", "BOTTOM", "BOUGHT", "BRANCH", "BREATH", "BRIDGE", "BRIGHT", "BROKEN", "BUDGET", "BURDEN", "BUREAU", "BUTTON", "CAMERA", "CANCER", "CANNOT", "CARBON", "CAREER", "CASTLE", "CASUAL", "CAUGHT", "CENTER", "CENTRE", "CHANCE", "CHANGE", "CHARGE", "CHOICE", "CHOOSE", "CHOSEN", "CHURCH", "CIRCLE", "CLIENT", "CLOSED", "CLOSER", "COFFEE", "COLUMN", "COMBAT", "COMING", "COMMON", "COMPLY", "COPPER", "CORNER", "COSTLY", "COUNTY", "COUPLE", "COURSE", "COVERS", "CREATE", "CREDIT", "CRISIS", "CUSTOM", "DAMAGE", "DANGER", "DEALER", "DEBATE", "DECADE", "DECIDE", "DEFEAT", "DEFEND", "DEFINE", "DEGREE", "DEMAND", "DEPEND", "DEPUTY", "DESERT", "DESIGN", "DESIRE", "DETAIL", "DETECT", "DEVICE", "DIFFER", "DINNER", "DIRECT", "DOCTOR", "DOLLAR", "DOMAIN", "DOUBLE", "DRIVEN", "DRIVER", "DURING", "EASILY", "EATING", "EDITOR", "EFFECT", "EFFORT", "EIGHTH", "EITHER", "ELEVEN", "EMERGE", "EMPIRE", "EMPLOY", "ENABLE", "ENDING", "ENERGY", "ENGAGE", "ENGINE", "ENOUGH", "ENSURE", "ENTIRE", "ENTITY", "EQUITY", "ESCAPE", "ESTATE", "ETHNIC", "EXCEED", "EXCEPT", "EXCESS", "EXPAND", "EXPECT", "EXPERT", "EXPORT", "EXTEND", "EXTENT", "FABRIC", "FACING", "FACTOR", "FAILED", "FAIRLY", "FALLEN", "FAMILY", "FAMOUS", "FATHER", "FELLOW", "FEMALE", "FIGURE", "FILING", "FINGER", "FINISH", "FISCAL", "FLIGHT", "FLYING", "FOLLOW", "FORCED", "FOREST", "FORGET", "FORMAL", "FORMAT", "FORMER", "FOSTER", "FOUGHT", "FOURTH", "FRENCH", "FRIEND", "FUTURE", "GARDEN", "GATHER", "GENDER", "GERMAN", "GLOBAL", "GOLDEN", "GROUND", "GROWTH", "GUILTY", "HANDED", "HANDLE", "HAPPEN", "HARDLY", "HEADED", "HEALTH", "HEIGHT", "HIDDEN", "HOLDER", "HONEST", "IMPACT", "IMPORT", "INCOME", "INDEED", "INJURY", "INSIDE", "INTEND", "INTENT", "INVEST", "ISLAND", "ITSELF", "JERSEY", "JOSEPH", "JUNIOR", "KILLED", "LABOUR", "LATEST", "LATTER", "LAUNCH", "LAWYER", "LEADER", "LEAGUE", "LEAVES", "LEGACY", "LENGTH", "LESSON", "LETTER", "LIGHTS", "LIKELY", "LINKED", "LIQUID", "LISTEN", "LITTLE", "LIVING", "LOSING", "LUCENT", "LUXURY", "MAINLY", "MAKING", "MANAGE", "MANNER", "MANUAL", "MARGIN", "MARINE", "MARKED", "MARKET", "MARTIN", "MASTER", "MATTER", "MATURE", "MEDIUM", "MEMBER", "MEMORY", "MENTAL", "MERELY", "MERGER"]
  },
}


def shuffle_word(word):
  word = list(word)
  shuffle(word)
  return ''.join(word)

def jumbleword(words= ''):
  shuffleword= shuffle_word(words)
  if shuffleword == words:
    shuffleword= jumbleword(words)
  return shuffleword

def wordgame(lvl= "easy"):
  global started, activeword
  started= True
  words= level[lvl]["words"]
  activeword= choice(words)
  print(jumbleword(activeword))


def game(u_input):
  global score, times, lvl
  if welcomeshown == False:
    welcome()
    return

  if started == False and (u_input not in commands):
    print("Enter 'S' to start or 'X' to exit")
    return

  if times == lives:
    u_input= "X"
    return 0

  if u_input == "s" or u_input == "S":
    wordgame();
  elif u_input == "r" or u_input == "R":
    reset();
    welcome();
  elif u_input == "v" or u_input == "V":
    print("Your current score is ",score)
  elif u_input == "x" or u_input == "X":
    print("Your score is ",score,". Thank you for playing, hoping you try again soon!")
    reset();
  else:
    if activeword == u_input.upper():
      score += 1 # score = score + 1
      if score > 3:
        lvl= "medium"
      elif score > 7:
        lvl= "hard"
    else:
      times += 1
      print("Sorry, that is the wrong answer. The correct answer is ",activeword)
    print("Moving to the next word")
    wordgame(lvl)
     
import threading

   
while(True):
  u_input = input()
  k = 0
  
  def end():
    global k
    k = 1
    print

  timer = threading.Timer(10.0, end)

  if(k == 1):
    break
  
    
  if u_input=='x' or u_input=="X":
    print("Exitting Game ...")
    break
  loose = game(u_input)
  if loose == 0:
    print("Max lives used !")
    break