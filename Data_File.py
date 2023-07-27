list_features = '''
1. Online Course Recommendator - '/onlinecourse'
2. YouTube Course Recommendator - '/youtubecourse'
3. Cheat Sheets - '/cheatsheet'
4. GitHub Learning Resources - '/githublearn'
5. External Mark Needed for Specific Grade - '/gradecalculator'
6. Playback Speed Calculator - '/playbackspeedcalculator'
7. Password Generator - '/password'
8. Text to Audio Converter - '/textaudio'
9. QR Code Generator - '/qrcodegenerator'
10. Morse Code Generator - '/morsecode'
11. Weather Details of Your Current Location - '/weather'
12. Random Activity Generator - '/activity'
13. Syllabus Sender - '/syllabus'
14. Latest news Sender - '/news'
15. Linux Distro Recommendator - '/linuxdistro'
16. Linux Command PDF - '/linuxcommandpdf'
17. Ask Me a Joke - '/joke'
18. Roll a Dice - '/dice'
19. Corporate BS - '/corporatebs'
20. Superhero Details - '/super'
21. Random Meme Generator - '/meme'
'''

#################Possible keywords for each command ###################################
online_course_possible_keywords = ['online course', 'udemy', 'coursera', 'onlinecourse', 'online cors',
                                    'onlie course', 'ondline course', 'oneline course', 'udamy', 'udmey',
                                    'udemu', 'courseraa', 'corsera', 'coursesra', 'onlinecouse', 'onlinecoarse',
                                    'onlinecours', 'onlnie course', 'onilne course', 'onlne course', 'ondilne course',
                                    'onlinne course', 'udemmy', 'udemyy', 'udemyy', 'courser', 'couser', 'corusera']

youtube_course_possible_keywords = ['youtube','yutube', 'youtub', 'uoutube', 'youtibe', 'yuotube', 
                                    'youtuube', 'youtubee', 'youtbe', 'youtubr', 'yuotube', 
                                    'youtub', 'youtubbe', 'youtupe', 'youtub3', 'youtibe', 
                                    'youube', 'yooutube', 'youtub4', 'youtbue']

cheat_sheet_possible_keywords = ['cheat sheet', 'cheatsheet', 'cheet sheet', 'cheetshet', 'cheetseet', 'cheat seet',
                                'cheat shet', 'cheet sheat', 'cheetsheet', 'cheetshett', 'cheetseett', 'cheet seett',
                                'cheet shett', 'cheet sheatt', 'cheatsheeet', 'cheatshett', 'cheat sheat', 'cheetsheatt',
                                'cheatsheett', 'cheat sheatt']

github_learn_possible_keywords = ['github', 'github learn', 'github resources', 'git hub', 'git hub learn', 'git hub resources',
                                'github learn', 'github resources', 'github learn', 'github resources', 'gith ub', 'gith ub learn',
                                'gith ub resources', 'git-hub', 'git-hub learn', 'git-hub resources', 'githublearn', 'githubresources',
                                'git hublearn', 'git hubresources']

external_mark_calculator_possbile_keywords = ['grade', 'external mark', 'internal mark', 'externalmark', 'internalmark', 'grad',
                                            'externl mark', 'internal mrk', 'externlmark', 'internlmark', 'external assessment',
                                            'internal assessment', 'external marking', 'internal marking', 'garde', 'external marks',
                                            'internal marks', 'externalmarks', 'internalmarks', 'grde', 'externel mark', 'internel mark', 
                                            'externelmark', 'internlmark', 'externl assessment', 'external marking', 'internal marking']

playback_speed_possible_keywords = ['speed', 'playbackspeed', 'play back speed', 'play backspeed', 'playback speed', 'sped', 'playbakspeed',
                                     'play bak speed', 'play back sped', 'playbak sped', 'playbak sped', 'play bak speed']

password_generator_possible_keywords = ['password', 'passwordgenerator', 'password generator', 'pssword', 'passwordgeneratr', 
                                        'password generatr', 'pasword', 'passwordgeneraotr', 'password generaotr']

text_to_audio_possible_keywords = ['text to audio', 'audio', 'texttoaudio', 'txt to audio', 'audi', 'texttoaudi', 'text toaudi', 'text 2 audio',
                                    'audio text', 'text2audio', 'audio', 'txt 2 audio', 'audi', 'text2audi', 'text 2audi', 'text-to-audio', 'audio',
                                    'text-to-audio', 'txt-to-audio', 'audi', 'texttoaudio', 'text-toaudio', 'text to audio', 'audio', 'texttoaudio',
                                    'txt to audio', 'audi', 'texttoaudi', 'text toaudi', 'txt2audio', 'aud', 'text-toaudio', 'text 2-audio', 'aud',
                                    'text2-audio', 'audio text', 'txt2-audio', 'text 2audio', 'audio-text', 'text2audio']

qr_code_generator_possible_keywords = ['qr', 'qr code', 'qrcode', 'q-r', 'q-r code', 'qr-code']

morse_code_generator_possible_keywords = ['morse', 'morse code', 'morsecode', 'morze', 'morze code',
                                        'morzecode', 'mors', 'mors code', 'morscode']

weather_possible_keywords = ['weather', 'temperature', 'humidity', 'rain', 'location', 'wether', 'temprature', 'humidity', 'rane', 'loction',
                            'weathr', 'tempreture', 'humidity', 'rein', 'locatin', 'weathe', 'temperatur', 'humidty', 'locaton', 'wather',
                            'temparature', 'hmidity', 'raain', 'locaion', 'waether', 'temperatue', 'humidy', 'rainn', 'lcoation',
                            'wahter', 'temperate', 'hunidity', 'lcation', 'weatther', 'temperture', 'humididy', 'rean', 'locatioon', 'wethr',
                            'tmeperature', 'hmidty', 'ranin']

random_activity_possible_keywords = ['activity', 'task', 'activty', 'taks', 'actvity']

st_thomas_syllabus_possible_keywords = ['syllabus', 'curriculum', 'syllbus', 'curiculum', 'silabus', 'curruculum', 'program', 'course outline', 
                                    'study plan', 'subject matter', 'lesson plan', 'outline' , 'syllab', 
                                    'curriculm', 'syllabu', 'curricum', 'sylabus', 'curruculm', 'sylabus', 'curruculum', 'syllabs', 'curriculam', 'silabas',
                                    'curruculam', 'silabus', 'curriculum', 'syllbass', 'curruculm', 'sylabas', 'curruculum']
st_thomas_news_sender_possible_keywords = ["nwes","neew","nws","newz","neew","niew","neew","knws","nwez","neew","newz"
                                           "nwss","neus","newx","nuws","naws","bews","nwes","neas","bews","neas","nwws","neas","nrw",
                                            "nees","neas","neqs","neqs","nrws","news","newx","naws","nebs","news","nrrw",]
linux_distro_reccomendator_possible_keywords = ['distro','linux distro', 'linuxdistro', 'linx distro', 'linxdistro', 'linu distro', 'linudistro', 'lnux distro', 
                                                'lnuxdistro', 'linux disto', 'linuxdistr', 'linux distor', 'linuxdistro']

linux_commands_pdf_sender_possible_keywords = ['command','linuxcommand', 'linux command', 'linux commands', 'linuxcommands', 'linxcommand', 'linx command', 'linx commands',
                                                'linxcommands', 'linu command', 'linu commands', 'lnux command', 'lnux commands', 'linux comand', 'linux comands', 
                                                'linuxcomand', 'linuxcomands']

random_joke_possible_keywords = ['joke', 'comedy', 'jok', 'comdy', 'jooke', 'comedi', 'jok', 'comdy', 'joek', 'comdey', 'joake', 'comdei']

Dice_possible_keywords = ['dice', 'die', 'gambling cube', 'game of chance', 'random number generator', 'dice roll', 'dice game',
                           'rolling the dice', 'craps']

Coporate_bs_possible_keywords = ['bs', 'bullshit', 'busswords', 'bussword', 'buzzwords', 'coporate bs', 'coporatebs', 'bull shit',
                 'buswords', 'busword', 'buzwords', 'cporate bs', 'cporatebs', 'bulshit']

super_hero_possible_keywords = ['hero', 'super', 'superhero', 'super hero', 'heroe', 'supr', 'suprhero', 'supr hero',
                                'herro', 'sper', 'sperhero', 'sper hero']

Random_meme_possible_keywords = ['meme']
#######################################################################################
Online_course_Python_Udemy = ("https://www.udemy.com/course/100-days-of-code",
    "https://www.udemy.com/course/complete-python-bootcamp/",
    "https://www.udemy.com/course/complete-python-developer-zero-to-mastery/",
    "https://www.udemy.com/course/the-modern-python3-bootcamp/",
    "https://www.udemy.com/course/python3-fundamentals/",
    "https://www.udemy.com/course/total-python/",
    "https://www.udemy.com/course/python-core-and-advanced/",
    "https://www.udemy.com/course/python-for-absolute-beginners-u/",
    "https://www.udemy.com/course/python-the-complete-python-developer-course/",
    "https://www.udemy.com/course/complete-python-developer-zero-to-master")
Online_course_Python_Coursera = ("https://www.coursera.org/specializations/python-3-programming",
    "https://www.coursera.org/learn/python-crash-course",
    "https://www.coursera.org/learn/python-for-applied-data-science-ai",
    "https://www.coursera.org/learn/get-started-with-python",
    "https://www.coursera.org/learn/python-programming-intro",
    "https://www.coursera.org/specializations/python-3-programming",
    "https://www.coursera.org/learn/python-crash-course",
    "https://www.coursera.org/learn/python-for-applied-data-science-ai",
    "https://www.coursera.org/learn/get-started-with-python",
    "https://www.coursera.org/learn/python-programming-intro")

Online_course_Java_Udemy = ("https://www.udemy.com/course/java-the-complete-java-developer-course/",
    "https://www.udemy.com/course/java-se-programming/",
    "https://www.udemy.com/course/java-programming-tutorial-for-beginners/",
    "https://www.udemy.com/course/the-complete-java-development-bootcamp/",
    "https://www.udemy.com/course/full-stack-java-developer-java/",
    "https://www.udemy.com/course/java-development-for-beginners-learnit/",
    "https://www.udemy.com/course/java-programming-complete-beginner-to-advanced/",
    "https://www.udemy.com/course/master-practical-java-development/",
    "https://www.udemy.com/course/practical-java-course/",
    "https://www.udemy.com/course/java-11-complete-beginners/")
Online_course_Java_Coursera = ("https://www.coursera.org/specializations/javascript-beginner",
    "https://www.coursera.org/learn/html-css-javascript-for-web-developers",
    "https://www.coursera.org/learn/programming-with-javascript",
    "https://www.coursera.org/learn/javascript-basics",
    "https://www.coursera.org/learn/learn-javascript",
    "https://www.coursera.org/specializations/javascript-beginner",
    "https://www.coursera.org/learn/html-css-javascript-for-web-developers",
    "https://www.coursera.org/learn/programming-with-javascript",
    "https://www.coursera.org/learn/javascript-basics",
    "https://www.coursera.org/learn/learn-javascript")

Online_course_Javascript_Udemy = ("https://www.udemy.com/course/the-complete-javascript-course/",
    "https://www.udemy.com/course/the-complete-web-development-bootcamp/",
    "https://www.udemy.com/course/javascript-the-complete-guide-2020-beginner-advanced/",
    "https://www.udemy.com/course/advanced-javascript-concepts/",
    "https://www.udemy.com/course/javascript-basics-for-beginners/",
    "https://www.udemy.com/course/javascript-beginners-complete-tutorial/",
    "https://www.udemy.com/course/modern-javascript-from-the-beginning/",
    "https://www.udemy.com/course/javascript-tutorial-for-beginners-w/",
    "https://www.udemy.com/course/js-algorithms-and-data-structures-masterclass/",
    "https://www.udemy.com/course/the-complete-web-developer-zero-to-mastery/"
)
Online_course_Javascript_Coursera = ("https://www.coursera.org/specializations/javascript-beginner",
    "https://www.coursera.org/learn/html-css-javascript-for-web-developers",
    "https://www.coursera.org/learn/programming-with-javascript",
    "https://www.coursera.org/learn/javascript-basics",
    "https://www.coursera.org/learn/learn-javascript",
    "https://www.coursera.org/specializations/javascript-beginner",
    "https://www.coursera.org/learn/html-css-javascript-for-web-developers",
    "https://www.coursera.org/learn/programming-with-javascript",
    "https://www.coursera.org/learn/javascript-basics",
    "https://www.coursera.org/learn/learn-javascript")

Online_course_C_Udemy = ( "https://www.udemy.com/course/the-complete-web-developer-zero-to-mastery/",
    "https://www.udemy.com/course/beginning-c-plus-plus-programming/",
    "https://www.udemy.com/course/cpp-deep-dive/",
    "https://www.udemy.com/course/the-modern-cpp-20-masterclass/",
    "https://www.udemy.com/course/beg-modern-cpp/",
    "https://www.udemy.com/course/learn-c-and-c-beginner-to-advance/",
    "https://www.udemy.com/course/c-coding-learn-c-programming-with-examples-in-one-day/",
    "https://www.udemy.com/course/the-complete-cpp-developer-course/",
    "https://www.udemy.com/course/quick-start-to-modern-c-for-programmers/",
    "https://www.udemy.com/course/cplusplus-programming-step-by-step/")
Online_course_C_Coursera = ("https://www.coursera.org/specializations/coding-for-everyone",
    "https://www.coursera.org/specializations/c-programming",
    "https://www.coursera.org/specializations/hands-on-cpp",
    "https://www.coursera.org/learn/programming-languages-part-c",
    "https://www.coursera.org/specializations/cplusplusunrealgamedevelopment",
    "https://www.coursera.org/specializations/coding-for-everyone",
    "https://www.coursera.org/specializations/c-programming",
    "https://www.coursera.org/specializations/hands-on-cpp",
    "https://www.coursera.org/learn/programming-languages-part-c",
    "https://www.coursera.org/specializations/cplusplusunrealgamedevelopment")


Youtube_video_python = ("https://www.youtube.com/watch?v=_uQrJ0TkZlc&pp=ygUHUHl0aG9uIA%3D%3D",
    "https://www.youtube.com/watch?v=7wnove7K-ZQ&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg",
    "https://www.youtube.com/watch?v=VchuKL44s6E&pp=ygUHUHl0aG9uIA%3D%3D",
    "https://www.youtube.com/watch?v=rfscVS0vtbw&pp=ygUOUHl0aG9uICBjb3Vyc2U%3D",
    "https://www.youtube.com/watch?v=6i3EGqOBRiU&list=PLdo5W4Nhv31bZSiqiOL5ta39vSnBxpOPT",
    "https://www.youtube.com/watch?v=XKHEtdqhLK8&pp=ygUOUHl0aG9uICBjb3Vyc2U%3D",
    "https://www.youtube.com/watch?v=mRMmlo_Uqcs&list=PLIhvC56v63ILPDA2DQBv0IKzqsWTZxCkp",
    "https://www.youtube.com/watch?v=nLRL_NcnK-4&pp=ygUOUHl0aG9uICBjb3Vyc2U%3D",
    "https://www.youtube.com/watch?v=sxTmJE4k0ho&pp=ygUOUHl0aG9uICBjb3Vyc2U%3D",
    "https://www.youtube.com/watch?v=fqF9M92jzUo&t=4s&pp=ygUOUHl0aG9uICBjb3Vyc2U%3D")

Youtube_video_Java = ("https://www.youtube.com/watch?v=yRpLlJmRo2w&list=PLfqMhTWNBTe3LtFWcvwpqTkUSlB32kJop",
    "https://www.youtube.com/watch?v=eIrMbAQSU34&pp=ygUMSmF2YSAgY291cnNl",
    "https://www.youtube.com/watch?v=BGTx91t8q50&pp=ygUMSmF2YSAgY291cnNl",
    "https://www.youtube.com/watch?v=VHbSopMyc4M&list=PLBlnK6fEyqRjKA_NuK9mHmlk0dZzuP1P5",
    "https://www.youtube.com/watch?v=wdkP056q0Nc&pp=ygUMSmF2YSAgY291cnNl",
    "https://www.youtube.com/watch?v=grEKMHGYyns&pp=ygUMSmF2YSAgY291cnNl",
    "https://www.youtube.com/watch?v=RJ733wzbNoA&list=PLxgZQoSe9cg00xyG5gzb5BMkOClkch7Gr",
    "https://www.youtube.com/watch?v=j9VNCI9Xo80&pp=ygUMSmF2YSAgY291cnNl",
    "https://www.youtube.com/watch?v=drQK8ciCAjY&pp=ygUMSmF2YSAgY291cnNl",
    "https://www.youtube.com/watch?v=UmnCZ7-9yDY&t=433s&pp=ygUMSmF2YSAgY291cnNl")

Youtube_video_Javascript =(
    "https://www.youtube.com/watch?v=ER9SspLe4Hg&list=PLu0W_9lII9ahR1blWXxgSlL4y9iQBnLpR",
    "https://www.youtube.com/watch?v=W6NZfCO5SIk&pp=ygURamF2YXNjcmlwdCBjb3Vyc2U%3D",
    "https://www.youtube.com/watch?v=PkZNo7MFNFg&pp=ygURamF2YXNjcmlwdCBjb3Vyc2U%3D",
    "https://www.youtube.com/watch?v=SBmSRK3feww&pp=ygURamF2YXNjcmlwdCBjb3Vyc2U%3D",
    "https://www.youtube.com/watch?v=jS4aFq5-91M&pp=ygURamF2YXNjcmlwdCBjb3Vyc2U%3D",
    "https://www.youtube.com/watch?v=Qqx_wzMmFeA&pp=ygURamF2YXNjcmlwdCBjb3Vyc2U%3D",
    "https://www.youtube.com/watch?v=lI1ae4REbFM&t=76s&pp=ygURamF2YXNjcmlwdCBjb3Vyc2U%3D",
    "https://www.youtube.com/watch?v=acUEBly28UU&pp=ygURamF2YXNjcmlwdCBjb3Vyc2U%3D",
    "https://www.youtube.com/watch?v=IC5vBKc21X8&pp=ygURamF2YXNjcmlwdCBjb3Vyc2U%3D",
    "https://www.youtube.com/watch?v=8dWL3wF_OMw&pp=ygURamF2YXNjcmlwdCBjb3Vyc2U%3D"
)

Youtube_video_C = ("https://www.youtube.com/watch?v=z9bZufPHFLU&list=PLfqMhTWNBTe0b2nM6JHVCnAkhQRGiZMSJ",
    "https://www.youtube.com/watch?v=vLnPwxZdW4Y&pp=ygUPYysrIGZ1bGwgY291cnNl",
    "https://www.youtube.com/watch?v=8jLOx1hD3_o&pp=ygUPYysrIGZ1bGwgY291cnNl",
    "https://www.youtube.com/watch?v=ZzaPdXTrSb8&pp=ygUPYysrIGZ1bGwgY291cnNl",
    "https://www.youtube.com/watch?v=-TkoO8Z07hI&pp=ygUPYysrIGZ1bGwgY291cnNl",
    "https://www.youtube.com/watch?v=oOmbSpOzvYg&list=PLdo5W4Nhv31YU5Wx1dopka58teWP9aCee",
    "https://www.youtube.com/watch?v=WQoB2z67hvY&list=PLDzeHZWIZsTryvtXdMr6rPh4IDexB5NIA",
    "https://www.youtube.com/watch?v=iOfUlcUy0as&pp=ygUPYysrIGZ1bGwgY291cnNl",
    "https://www.youtube.com/watch?v=FpfHmAkRVK4&pp=ygUPYysrIGZ1bGwgY291cnNl",
    "https://www.youtube.com/watch?v=bL-o2xBENY0&list=PLxgZQoSe9cg0df_GxVjz3DD_Gck5tMXAd")

Cheat_sheet_Python = "https://cheatography.com/davechild/cheat-sheets/python/pdf/"
Cheat_sheet_Java = "https://cheatography.com/sschaub/cheat-sheets/java-fundamentals/pdf/"
Cheat_sheet_Javascript = "https://cheatography.com/pyro19d/cheat-sheets/javascript/pdf/"
Cheat_sheet_Cpp = "https://cheatography.com/pmg/cheat-sheets/c/pdf/" 
Cheat_sheet_Git = "https://cheatography.com/samcollett/cheat-sheets/git/pdf/"

morse_dicitonary = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}

## Syllabus Finder###
Data_science_bvoc_data_science = "https://stthomas.ac.in/wp-content/uploads/2021/12/B.Voc-Data-Science.pdf"
botany_bsc_botany = "https://stthomas.ac.in/wp-content/uploads/2021/12/BSc-Botany.pdf"
botany_msc_botany = "https://stthomas.ac.in/wp-content/uploads/2021/12/M-Sc-botany.pdf"
chemistry_bsc_chem = "https://stthomas.ac.in/wp-content/uploads/2021/12/BSc-Chem.pdf"
chemistry_msc_chem = "https://stthomas.ac.in/wp-content/uploads/2021/12/MSc-Chemistry.pdf"
commerce_mcom = "https://stthomas.ac.in/wp-content/uploads/2021/12/MCom.pdf"
commerce_bcom_finance = "https://stthomas.ac.in/wp-content/uploads/2021/12/BCom-Finance.pdf"
commerce_bcom_banking = "https://stthomas.ac.in/wp-content/uploads/2021/12/BCom-Banking.pdf"
commerce_sf_bcom ="https://stthomas.ac.in/wp-content/uploads/2020/08/B-Com1.pdf"
computer_application_bca = "https://stthomas.ac.in/wp-content/uploads/2021/12/BCA.pdf"
computer_application_msc_cs = "https://stthomas.ac.in/wp-content/uploads/2021/12/MSc-Computer-Science.pdf"
computer_science_bsc_cs = "https://stthomas.ac.in/wp-content/uploads/2022/01/Computer-Science-Final.pdf"
computer_science_msc_cs = "https://stthomas.ac.in/wp-content/uploads/2021/12/MSc-Computer-Science.pdf"
criminology_ba_criminology = "https://stthomas.ac.in/wp-content/uploads/2021/12/Criminology.pdf"
economics_ba_economics = "https://stthomas.ac.in/wp-content/uploads/2021/12/BA-Economics.pdf"
economics_ma_economics = "https://stthomas.ac.in/wp-content/uploads/2021/12/MA-Economics-1.pdf"
electronics_bsc_electronics = "https://stthomas.ac.in/wp-content/uploads/2021/12/BSc-Electronics.pdf"
electronics_msc_electronics= "https://stthomas.ac.in/wp-content/uploads/2021/12/MSC-Electronics.pdf"
english_ba_english = "https://stthomas.ac.in/wp-content/uploads/2021/12/BA-English-.pdf"
english_ba_double_main = "https://stthomas.ac.in/wp-content/uploads/2021/12/BA-Double-Main.pdf"
english_ma_english = "https://stthomas.ac.in/wp-content/uploads/2021/12/MA-English.pdf"
FS_bvoc_forensic_science = "https://stthomas.ac.in/wp-content/uploads/2021/12/Bvoc-Forensic-Science.pdf"
MS_bba = "https://stthomas.ac.in/wp-content/uploads/2021/12/BBA.pdf"
Maths_bsc_mathematics = "https://stthomas.ac.in/wp-content/uploads/2021/12/BSc-Mathematics.pdf"
Maths_msc_mathematics = "https://stthomas.ac.in/wp-content/uploads/2021/12/MSc-Mathematics-.pdf"
Media_ba_visual_communication = "https://stthomas.ac.in/wp-content/uploads/2021/12/BA-Visual-Communication.pdf"
Media_ba_multimedia = "https://stthomas.ac.in/wp-content/uploads/2021/12/BA-Multimedia.pdf"
Media_ma_visual_communication = "https://stthomas.ac.in/wp-content/uploads/2021/12/MA-Visual-Communication.pdf"
Physics_bsc_physics = "https://stthomas.ac.in/wp-content/uploads/2021/12/BSc-Physics.pdf"
Physics_msc_physics = "https://stthomas.ac.in/wp-content/uploads/2021/12/M.Sc_.-Physics.pdf"
Psychology_integrated_msc_psychology = "https://stthomas.ac.in/wp-content/uploads/2022/01/Integrated-MSc-Psychology.pdf"
SW_msw = "https://stthomas.ac.in/wp-content/uploads/2021/12/MSW.pdf"
Stati_bsc_statistics = "https://stthomas.ac.in/wp-content/uploads/2021/12/BSc-Statistics-Updated.pdf"
Stati_msc_statistics = "https://stthomas.ac.in/wp-content/uploads/2021/12/MSc-Statistics.pdf"
Zoology_bsc_zoology = "https://stthomas.ac.in/wp-content/uploads/2021/12/BSc-Zoology.pdf"
Zoology_msc_zoology = "https://stthomas.ac.in/wp-content/uploads/2021/12/Msc-Zoology.pdf"

#####################

###Linux distro recomendator data ###
linux_distro_recomendator_beginners = "1. Ubuntu\n2. Linux Mint\n3. Zorin OS\n4. Elementary OS\n5. Linux Lite\n6. Manjaro Linux\n7. Pop!_OS\n8. Peppermint OS\n9. Deepin"
linux_distro_recomendator_gamers = "1. Fedora\n2. Garuda Linux\n3. Pop!_OS\n4. Ubuntu\n5. Drauger OS\n6. Regata OS\n7. SteamOS (Holo ISO)\n8. Manjaro\n9. Linux Mint\n10. Lakka Linux"
linux_distro_recomendator_proffesional_use = "1. Debian Linux\n 2. Manjaro Linux\n3. AlmaLinux/Rocky Linux\n4. Ubuntu\n5. OpenSUSE\n 6. Linux Mint"
linux_distro_recomendator_low_spec_system = '''1. Tiny Core
2. Puppy Linux
3. SparkyLinux
4. antiX Linux
5. Bodhi Linux
6. CrunchBang++
7. LXLE
8. Linux Lite
9. Lubuntu
10. Peppermint
11. Linux Mint Xfce
12. Xubuntu
13. Zorin OS Lite
14. Ubuntu MATE
15. Slax
16. Q4OS'''
linux_distro_recomendator_hackers = "1. Kali Linux\n2. BackBox\n3. ParrotOS\n4. BlackArch\n5. Samurai Web Testing Framework\n6. Pentoo Linux\n7. CAINE\n8. Network Security Toolkit\n9. Fedora Security Spin\n10. ArchStrike"
linux_distro_recomendator_developers = "1. Manjaro\n2. Ubuntu\n3. Pop!_OS\n4. Debian\n5. openSUSE\n6. Arch Linux\n7. Fedora Workstation\n8. Kali Linux\n9. Raspberry Pi OS\n10. Solus OS"
#######################################
## linux commands pdf #############
linux_commands_pdf = "https://cheatography.com/davechild/cheat-sheets/linux-command-line/pdf/"
