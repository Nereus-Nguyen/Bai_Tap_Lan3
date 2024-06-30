# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
import re
data = "37107287533371072875339021027987979982208375902465101357402504637693767749000971264812489697007805041701826053874324986199524741059474233309513058123726617309629919422133635741615725224305633018110724061549082502306758820753934617117198031042104751377806324667689261670696623633820136378418383684178734361726757281128798128499794080654819315926216912758898327384427422891743252032192358942287679648767027218931847451445736001306439091167216856844588711603153276703864861058430254399396198289175936656867579349516217645714185656062950215722319658675507932419333164906352462741904929101432445813822663347944758178925758677183372176619637515905792397282455988384075820356532535939900840263356894883018945862822782880181199384826282014278194139940567587151170094390353986643728271126538299872407844730531901042935868651550600629586486153207527337195919142051725582971693888707715466499115593487603532921714970056938543700705768266846246214956500764717872944383776045328265410875682844319119063469403785521777929514536123272525000296071075082563815656710885258350721458765761724109764473391106072182652368772236360451742370690585186066044820762120981328786073396941281142660418086830619328460811191061556940512689692519343254517283886419180470492932150586425630494836246722164843507620172791803994469300473295634069115732444386908125794514089057706229429197107928209550376875256787730918625407449698445083303936821261833638482533015468619612434876768129753437594651580386287592878490201521685554828717201219257766954781828337579931036147403568564490955270978647975811672632010043689784255353992093183744149780686098448403098129077791799088218795327364475675590848030870869875513927118545170785441618524243206931503325995940689575653678210707492696653767632623544721069793950679652694742597709739166693763042633987085410526847082990852113994273657341161827603150012716537860736150108085700914993951255702819874600437535829035317434717326932123578154982629742552737307949537597651053059469660676831565743771674018752758890280257173322961917666871381993181104877019027125267680276078003013678680992525463401061632866526362702185404977055856299465806362379931407462559622407448690823117497779236546625724692332281091714191430288197103288597806669760892938638285025333403344130655780161278159218150055618688364684200904702305308117281643048762379196984248725503663878458311487696932154902810424020138335124462181441773470637832994906362596664985876182212252255124867645336772018697169854431241957240991395900895231005882295548255300263520781532296796249481641953868218774760853271322857231104248034561248676970645079952363777424253541129168427686553892620502491032657296723701913275725675285653248258265463092207058596522297988602722583319131263751473419948895347657455011849570145487928898485682772607771372140379887971538298203783031473527721580348144513491373226651381348295438291999181802789165224310273922511228695394095795306640523263253804410005965493915987959363529746152185502371307642255121183693803580388584903416981162220729771861582366784246891579935329619226246795719440126904387710727504810239089552359745723189706772547915061505504953922979530901129967519861880882258753145295840992512038290094077707756721130673970830472448381653387350234084564705807730882959174767140363198008187129011875491310547126581976233310448183862695154563349263665728975634005004284628018351707052783183942588214552122725125032755121603546981200581762165212827652751691296897789322381957343293399464375019078369457658833523998867550616496518477518073816883786109152735792970133762177842752192623401942399639168044983993173312731329241857071473495669166746876346609150359146775049951867143023521962889489010242332511691361962662273267460800591547471830798392868535206946944540724768418225246744171615140364279822733480555562148189714261791034259864720451689398942217982608807685287783646182799346313767754307809363333018982642090108488025216746708832151201858835432238128769527867132961247478246453863699300904931036361976387803962184073572399794223406235393808339651327408011116666278919814880877979418768761442300309844908514116066182629368283676474477923918033511098906979071485786944089552990653640447425576083659976645795096660243964099053896071201982199760475994901972302976491398268003297315603712004137790378556608508925216730939319872750275468906903707539413042652315011948093772450487951509541009216458637547105984367917863916702118749243199570064191796977759902830069915368713711936614952811305876380278410754449733078407899231155355625611423224232550336854424889173534488991150144064802036906806396067232219320414953541503128880339536053299340368006977710650566631954812348806732101467390585685579345814036278227032808261657077394832759223284594170652509451232523060822918802058777319719839450180888072429661980811197771585425020165450904132458097868827789487218596177210783843506918615543566288406225747369228450951620849603980134001723930671666823555245252804609722535035342264725242508740540755917897812643303316909021027987979982208375902465101357402504637693767749000971264812489697007805041701826053874324986199524741059474233309513058123726617309629919422133635741615725224305633018110724061549082502306758820753934617117198031042104751778063246676"
pattern = r".{50}"

chunks = re.findall(pattern, data)
for chunk in chunks:
    print(chunk)
    
    for i in chunk:
        tinh_tong = sum(map(int, chunk))
        
    print(tinh_tong)

