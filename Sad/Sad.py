# -*- coding: utf-8 -*-

import tweepy
import re

consumer_key = 'wDPlj513reBvpDflXKDbSK9lQ'

consumer_secret = 'wfKhCv3L0djCNPhTqNW2CyysKaLUP2ARgUE8h03UL8RtKjOckW'

access_token = '972705355154079744-Xch0ybmZ678I6ZkTOuK87E5mfuiYoH0'

access_token_secret = 'xeniK0Q09fwQtyiWNwLuQtNCcLTgrmHdxJOSvlN5yjP73'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def tweet_processing(t):
    t1 = re.sub(r"@\S+", "", t)
    t2 = re.sub(r"http\S+", "", t1)
    t3 = t2.strip()
    l = t3.splitlines()
    pt = ' '.join(l)
    return pt

location = "%s,%s,%s" % ("35.95", "128.25", "1000km")

keywords = ['"가슴아프다" OR "가슴아프네" OR "가슴아프군" OR "가슴아파" OR "가슴아픔" OR "가슴아픕니다" -"안가슴아" -filter:retweets',
            '"가슴아팠다" OR "가슴아팠네" OR "가슴아팠어" OR "가슴아팠음" OR "가슴아팠습니다" -"안가슴아팠" -filter:retweets',
            '"가슴앓이" -filter:retweets',
            '"각박하다" OR "각박하네" OR "각박하군" OR "각박해" OR "각박함" OR "각박합니다" -"안각박" -filter:retweets',
            '"각박했다" OR "각박했네" OR "각박했어" OR "각박했음" OR "각박했습니다" -"안각박" -"괜히각박했" -filter:retweets',
            '"걱정된다" OR "걱정되네" OR "걱정되군" OR "걱정되는군" OR "걱정돼" OR "걱정됨" OR "걱정됩니다" -"안걱정" -filter:retweets',
            '"고달프다" OR "고달프네" OR "고달프군" OR "고달퍼" OR "고달픔" OR "고달픕니다" -"안고달" -filter:retweets',
            '"고달팠다" OR "고달팠네" OR "고달팠어" OR "고달팠음" OR "고달팠습니다" -"안고달팠" -filter:retweets',
            '"고독하다" OR "고독하네" OR "고독하군" OR "고독해" OR "고독함" OR "고독합니다" -"안고독" -filter:retweets',
            '"고독했다" OR "고독했네" OR "고독했어" OR "고독했음" OR "고독했습니다" -"안고독" -"괜히고독했" -filter:retweets',
            '"공허하다" OR "공허하네" OR "공허하군" OR "공허해" OR "공허함" OR "공허합니다" -"안공허" -filter:retweets',
            '"공허했다" OR "공허했네" OR "공허했어" OR "공허했음" OR "공허했습니다" -"안공허" -"괜히공허했" -filter:retweets',
            '"괴롭다" OR "괴롭네" OR "괴롭군" OR "괴로워" OR "괴로움" OR "괴롭습니다" -"안괴로" -"안괴롭" -filter:retweets',
            '"괴로웠다" OR "괴로웠네" OR "괴로웠어" OR "괴로웠음" OR "괴로웠습니다" -"안괴로웠" -"괜히괴로웠" -filter:retweets',
            '"구슬프다" OR "구슬프네" OR "구슬프군" OR "구슬퍼" OR "구슬픔" OR "구슬픕니다" -"안구슬" -filter:retweets',
            '"구슬펐다" OR "구슬펐네" OR "구슬펐어" OR "구슬펐음" OR "구슬펐습니다" -"안구슬펐" -"괜히구슬펐" -filter:retweets',
            '"그리워한다" OR "그리워요" OR "그리워함" OR "그리워합니다" -"안그리워" -filter:retweets',
            '"근심스럽다" OR "근심스럽네" OR "근심스럽군" OR "근심스러워" OR "근심스러움" OR "근심스럽습니다" -"안근심스" -filter:retweets',
            '"근심스러웠다" OR "근심스러웠네" OR "근심스러웠어" OR "근심스러웠음" OR "근심스러웠습니다" -"안근심스러웠" -"괜히근심스러웠" -filter:retweets',
            '"기구하다" OR "기구하네" OR "기구하군" OR "기구해" OR "기구함" OR "기구합니다" -"안기구" -filter:retweets',
            '"기구했다" OR "기구했네" OR "기구했어" OR "기구했음" OR "기구했습니다" -"안기구" -filter:retweets',
            '"기운없다" OR "기운없네" OR "기운없군" OR "기운없어요" OR "기운없음" OR "기운없습니다" -"안기운없" -filter:retweets',
            '"낙담한다" OR "낙담함" OR "낙담합니다" -"안낙담" -filter:retweets',
            '"낙담했다" OR "낙담했네" OR "낙담했어" OR "낙담했음" OR "낙담했습니다" -"안낙담" -"괜히낙담했" -filter:retweets',
            '"낙망한다" OR "낙망함" OR "낙망합니다" -"안낙망" -filter:retweets',
            '"낙망했다" OR "낙망했네" OR "낙망했어" OR "낙망했음" OR "낙망했습니다" -"안낙망" -"괜히낙망했" -filter:retweets',
            '"낙심한다" OR "낙심함" OR "낙심합니다" -"안낙심" -filter:retweets',
            '"낙심했다" OR "낙심했네" OR "낙심했어" OR "낙심했음" OR "낙심했습니다" -"안낙심" -"괜히낙심했" -filter:retweets',
            '"망연자실하다" OR "망연자실하네" OR "망연자실하군" OR "망연자실해요" OR "망연자실함" OR "망연자실합니다" -"안망연자실" -filter:retweets',
            '"망연자실했다" OR "망연자실했네" OR "망연자실했어" OR "망연자실했음" OR "망연자실했습니다" -"안망연자실" -"괜히망연자실했" -filter:retweets',
            '"먹먹하다" OR "먹먹하네" OR "먹먹하군" OR "먹먹해" OR "먹먹함" OR "먹먹합니다" -"안먹먹" -filter:retweets',
            '"먹먹했다" OR "먹먹했네" OR "먹먹했어" OR "먹먹했음" OR "먹먹했습니다" -"안먹먹" -"괜히먹먹했" -filter:retweets',
            '"불행하다" OR "불행하네" OR "불행하군" OR "불행해" OR "불행함" OR "불행합니다" -"안불행" -filter:retweets',
            '"불행했다" OR "불행했네" OR "불행했어" OR "불행했음" OR "불행했습니다" -"안불행" -filter:retweets',
            '"비참하다" OR "비참하네" OR "비참하군" OR "비참해" OR "비참함" OR "비참합니다" -"안비참" -filter:retweets',
            '"비참했다" OR "비참했네" OR "비참했어" OR "비참했음" OR "비참했습니다" -"안비참" -filter:retweets',
            '"비탄하다" OR "비탄하네" OR "비탄하군" OR "비탄해" OR "비탄함" OR "비탄합니다" -"안비탄" -filter:retweets',
            '"비탄했다" OR "비탄했네" OR "비탄했어" OR "비탄했음" OR "비탄했습니다" -"안비탄" -filter:retweets',
            '"비통하다" OR "비통하네" OR "비통하군" OR "비통해" OR "비통함" OR "비통합니다" -"안비통" -filter:retweets',
            '"비통했다" OR "비통했네" OR "비통했어" OR "비통했음" OR "비통했습니다" -"안비통" -filter:retweets',
            '"뼈저리다" OR "뼈저리네" OR "뼈저리군" OR "뼈저려" OR "뼈저림" OR "뼈저립니다" -"안뼈저" -filter:retweets',
            '"사무친다" OR "사무치네" OR "사무치군" OR "사무치는군" OR "사무쳐" OR "사무침" OR "사무칩니다" -"안사무" -filter:retweets',
            '"사무쳤다" OR "사무쳤네" OR "사무쳤어" OR "사무쳤음" OR "사무쳤습니다" -"안사무쳤" -"괜히사무쳤" -filter:retweets',
            '"상실감" -filter:retweets',
            '"서럽다" OR "서럽네" OR "서럽군" OR "서러워" OR "서러움" OR "서럽습니다" -"안서럽" -filter:retweets',
            '"서러웠다" OR "서러웠네" OR "서러웠어" OR "서러웠음" OR "서러웠습니다" -"안서러웠" -"괜히서러웠" -filter:retweets',
            '"서운하다" OR "서운하네" OR "서운하군" OR "서운해" OR "서운함" OR "서운합니다" -"안서운" -filter:retweets',
            '"서운했다" OR "서운했네" OR "서운했어" OR "서운했음" OR "서운했습니다" -"안서운" -"괜히서운했" -filter:retweets',
            '"섭섭하다" OR "섭섭하네" OR "섭섭하군" OR "섭섭해" OR "섭섭함" OR "섭섭합니다" -"안섭섭" -filter:retweets',
            '"섭섭했다" OR "섭섭했네" OR "섭섭했어" OR "섭섭했음" OR "섭섭했습니다" -"안섭섭" -"괜히섭섭했" -filter:retweets',
            '"속상하다" OR "속상하네" OR "속상하군" OR "속상해" OR "속상함" OR "속상합니다" -"안속상" -filter:retweets',
            '"속상했다" OR "속상했네" OR "속상했어" OR "속상했음" OR "속상했습니다" -"안속상" -"괜히속상했" -filter:retweets',
            '"속앓이" -filter:retweets',
            '"숙연하다" OR "숙연하네" OR "숙연하군" OR "숙연해" OR "숙연함" OR "숙연합니다" -"안숙연" -filter:retweets',
            '"숙연했다" OR "숙연했네" OR "숙연했어" OR "숙연했음" OR "숙연했습니다" -"안숙연" -"괜히숙연했" -filter:retweets',
            '"슬프다" OR "슬프네" OR "슬프군" OR "슬퍼" OR "슬픕니다" -"안슬프" -"안슬퍼" -"안슬픕" -filter:retweets',
            '"슬펐다" OR "슬펐네" OR "슬펐어" OR "슬펐음" OR "슬펐습니다" -"안슬펐" -"괜히슬펐" -filter:retweets',
            '"실망스럽다" OR "실망스럽네" OR "실망스럽군" OR "실망스러워" OR "실망스러움" OR "실망스럽니다" -"안실망스" -filter:retweets',
            '"실망스러웠다" OR "실망스러웠네" OR "실망스러웠어" OR "실망스러웠음" OR "실망스러웠습니다" -"안실망스러웠" -"괜히실망스러웠" -filter:retweets',
            '"심각하다" OR "심각하네" OR "심각하군" OR "심각해" OR "심각함" OR "심각합니다" -"안심각" -filter:retweets',
            '"심각했다" OR "심각했네" OR "심각했어" OR "심각했음" OR "심각했습니다" -"안심각" -"괜히심각했" -filter:retweets',
            '"심란하다" OR "심란하네" OR "심란하군" OR "심란해" OR "심란함" OR "심란합니다" -"안심란" -filter:retweets',
            '"심란했다" OR "심란했네" OR "심란했어" OR "심란했음" OR "심란했습니다" -"안심란" -"괜히심란했" -filter:retweets',
            '"쓴웃음" -filter:retweets',
            '"쓸쓸하다" OR "쓸쓸하네" OR "쓸쓸하군" OR "쓸쓸해" OR "쓸쓸함" OR "쓸쓸합니다" -"안쓸쓸" -filter:retweets',
            '"쓸쓸했다" OR "쓸쓸했네" OR "쓸쓸했어" OR "쓸쓸했음" OR "쓸쓸했습니다" -"안쓸쓸" -filter:retweets',
            '"씁쓸하다" OR "씁쓸하네" OR "씁쓸하군" OR "씁쓸해" OR "씁쓸함" OR "씁쓸합니다" -"안씁쓸" -filter:retweets',
            '"씁쓸했다" OR "씁쓸했네" OR "씁쓸했어" OR "씁쓸했음" OR "씁쓸했습니다" -"안씁쓸" -filter:retweets',
            '"안타깝다" OR "안타깝네" OR "안타깝군" OR "안타까워" OR "안타까움" OR "안타깝습니다" -"안안타" -filter:retweets',
            '"안타까웠다" OR "안타까웠네" OR "안타까웠어" OR "안타까웠음" OR "안타까웠습니다" -"안안타까웠" -filter:retweets',
            '"암담하다" OR "암담하네" OR "암담하군" OR "암담해" OR "암담함" OR "암담합니다" -"안암담" -filter:retweets',
            '"암울하다" OR "암울하네" OR "암울하군" OR "암울해" OR "암울함" OR "암울합니다" -"안암울" -filter:retweets',
            '"애끓는다" OR "애끓네" OR "애끓는군" OR "애끓음" OR "애끓습니다" -"안애끓" -filter:retweets',
            '"애가끓는다" OR "애가끓네" OR "애가끓는군" OR "애가끓음" OR "애가끓습니다" -"안애가끓" -filter:retweets',
            '"애달프다" OR "애달프네" OR "애달프군" OR "애달파" OR "애달픔" OR "애달픕니다" -"안애달" -filter:retweets',
            '"애도한다" OR "애도해" OR "애도함" OR "애도합니다" -"안애도" -filter:retweets',
            '"애도했다" OR "애도했네" OR "애도했어" OR "애도했음" OR "애도했습니다" -"안애도" -filter:retweets',
            '"애석하다" OR "애석하네" OR "애석하군" OR "애석해" OR "애석함" OR "애석합니다" -"안애석" -filter:retweets',
            '"애석했다" OR "애석했네" OR "애석했어" OR "애석했음" OR "애석했습니다" -"안애석" -filter:retweets',
            '"애잔하다" OR "애잔하네" OR "애잔하군" OR "애잔해" OR "애잔함" OR "애잔합니다" -"안애잔" -filter:retweets',
            '"애잔했다" OR "애잔했네" OR "애잔했어" OR "애잔했음" OR "애잔했습니다" -"안애잔" -filter:retweets',
            '"애처롭다" OR "애처롭네" OR "애처롭군" OR "애처로워" OR "애처로움" OR "애처롭습니다" -"안애처" -filter:retweets',
            '"애처로웠다" OR "애처로웠네" OR "애처로웠어" OR "애처로웠음" OR "애처로웠습니다" -"안애처로웠" -filter:retweets',
            '"애통하다" OR "애통하네" OR "애통하군" OR "애통해" OR "애통함" OR "애통합니다" -"안애통" -filter:retweets',
            '"애통했다" OR "애통했네" OR "애통했어" OR "애통했음" OR "애통했습니다" -"안애통" -filter:retweets',
            '"야속하다" OR "야속하네" OR "야속하군" OR "야속해" OR "야속함" OR "야속합니다" -"안야속" -filter:retweets',
            '"야속했다" OR "야속했네" OR "야속했어" OR "야속했음" OR "야속했습니다" -"안야속" -"괜히야속했" -filter:retweets',
            '"외롭다" OR "외롭네" OR "외롭군" OR "외로워" OR "외롭습니다" -"안외로" -"안외롭" -filter:retweets',
            '"외로웠다" OR "외로웠네" OR "외로웠어" OR "외로웠음" OR "외로웠습니다" -"안외로웠" -"괜히외로웠" -filter:retweets',
            '"우울하다" OR "우울하네" OR "우울하군" OR "우울해" OR "우울함" OR "우울합니다" -"안우울" -filter:retweets',
            '"우울했다" OR "우울했네" OR "우울했어" OR "우울했음" OR "우울했습니다" -"안우울" -"괜히우울했" -filter:retweets',
            '"울었다" OR "울었네" OR "울었어" OR "울었음" OR "울었습니다" -"안울었" -"괜히울었" -filter:retweets',
            '"울먹였다" OR "울먹였네" OR "울먹였어" OR "울먹였음" OR "울먹였습니다" -"안울먹였" -"괜히울먹였" -filter:retweets',
            '"울며불며" -filter:retweets',
            '"울부짖음" -"안울부짖" -filter:retweets',
            '"울부짖었다" OR "울부짖었네" OR "울부짖었어" OR "울부짖었음" OR "울부짖었습니다" -"안울부짖었" -"괜히울부짖었" -filter:retweets',
            '"울적하다" OR "울적하네" OR "울적하군" OR "울적해" OR "울적함" OR "울적합니다" -"안울적" -filter:retweets',
            '"울적했다" OR "울적했네" OR "울적했어" OR "울적했음" OR "울적했습니다" -"안울적" -"괜히울적했" -filter:retweets',
            '"울컥한다" OR "울컥하네" OR "울컥하군" OR "울컥해" OR "울컥함" OR "울컥합니다" -"안울컥" -filter:retweets',
            '"울컥했다" OR "울컥했네" OR "울컥했어" OR "울컥했음" OR "울컥했습니다" -"안울컥" -"괜히울컥했" -filter:retweets',
            '"유감스럽다" OR "유감스럽네" OR "유감스럽군" OR "유감스러워" OR "유감스러움" OR "유감스럽습니다" -"안유감스" -filter:retweets',
            '"유감스러웠다" OR "유감스러웠네" OR "유감스러웠어" OR "유감스러웠음" OR "유감스러웠습니다" -"안유감스러웠" -filter:retweets',
            '"음울하다" OR "음울하네" OR "음울하군" OR "음울해" OR "음울함" OR "음울합니다" -"안음울" -filter:retweets',
            '"자책한다" OR "자책함" OR "자책합니다" -"안자책" -filter:retweets',
            '"자책했다" OR "자책했네" OR "자책했어" OR "자책했음" OR "자책했습니다" -"안자책" -"괜히자책했" -filter:retweets',
            '"자포자기했다" OR "자포자기했네" OR "자포자기했어" OR "자포자기했음" OR "자포자기했습니다" -"안자포자기" -filter:retweets',
            '"적적하다" OR "적적하네" OR "적적하군" OR "적적해" OR "적적함" OR "적적합니다" -"안적적" -filter:retweets',
            '"적적했다" OR "적적했네" OR "적적했어" OR "적적했음" OR "적적했습니다" -"안적적" -"괜히적적했" -filter:retweets',
            '"절규함" -"안절규" -filter:retweets',
            '"절규했다" OR "절규했네" OR "절규했어" OR "절규했음" OR "절규했습니다" -"안절규" -filter:retweets',
            '"절망함" -"안절망" -filter:retweets',
            '"절망했다" OR "절망했네" OR "절망했어" OR "절망했음" OR "절망했습니다" -"안절망" -"괜히절망했" -filter:retweets',
            '"착잡하다" OR "착잡하네" OR "착잡하군" OR "착잡해" OR "착잡함" OR "착잡합니다" -"안착잡" -filter:retweets',
            '"착잡했다" OR "착잡했네" OR "착잡했어" OR "착잡했음" OR "착잡했습니다" -"안착잡" -"괜히착잡했" -filter:retweets',
            '"참담하다" OR "참담하네" OR "참담하군" OR "참담해" OR "참담함" OR "참담합니다" -"안참담" -filter:retweets',
            '"참담했다" OR "참담했네" OR "참담했어" OR "참담했음" OR "참담했습니다" -"안참담" -"괜히참담했" -filter:retweets',
            '"창피하다" OR "창피하네" OR "창피하군" OR "창피해" OR "창피함" OR "창피합니다" -"안창피" -filter:retweets',
            '"창피했다" OR "창피했네" OR "창피했어" OR "창피했음" OR "창피했습니다" -"안창피" -"괜히창피했" -filter:retweets',
            '"처량하다" OR "처량하네" OR "처량하군" OR "처량해" OR "처량함" OR "처량합니다" -"안처량" -filter:retweets',
            '"처량했다" OR "처량했네" OR "처량했어" OR "처량했음" OR "처량했습니다" -"안처량" -"괜히처량했" -filter:retweets',
            '"처참하다" OR "처참하네" OR "처참하군" OR "처참해" OR "처참함" OR "처참합니다" -"안처참" -filter:retweets',
            '"처참했다" OR "처참했네" OR "처참했어" OR "처참했음" OR "처참했습니다" -"안처참" -"괜히처참했" -filter:retweets',
            '"초라하다" OR "초라하네" OR "초라하군" OR "초라해" OR "초라함" OR "초라합니다" -"안초라" -filter:retweets',
            '"초라했다" OR "초라했네" OR "초라했어" OR "초라했음" OR "초라했습니다" -"안초라" -"괜히초라했" -filter:retweets',
            '"측은하다" OR "측은하네" OR "측은하군" OR "측은해" OR "측은함" OR "측은합니다" -"안측은" -filter:retweets',
            '"측은했다" OR "측은했네" OR "측은했어" OR "측은했음" OR "측은했습니다" -"안측은" -"괜히측은했" -filter:retweets',
            '"침울하다" OR "침울하네" OR "침울하군" OR "침울해" OR "침울함" OR "침울합니다" -"안침울" -filter:retweets',
            '"침울했다" OR "침울했네" OR "침울했어" OR "침울했음" OR "침울했습니다" -"안침울" -"괜히침울했" -filter:retweets',
            '"침통하다" OR "침통하네" OR "침통하군" OR "침통해" OR "침통함" OR "침통합니다" -"안침통" -filter:retweets',
            '"침통했다" OR "침통했네" OR "침통했어" OR "침통했음" OR "침통했습니다" -"안침통" -"괜히침통했" -filter:retweets',
            '"탄식함" -"안탄식" -filter:retweets',
            '"탄식했다" OR "탄식했네" OR "탄식했어" OR "탄식했음" OR "탄식했습니다" -"안탄식" -"괜히탄식했" -filter:retweets',
            '"통탄하다" OR "통탄하네" OR "통탄하군" OR "통탄해" OR "통탄함" OR "통탄합니다" -"안통탄" -filter:retweets',
            '"통탄했다" OR "통탄했네" OR "통탄했어" OR "통탄했음" OR "통탄했습니다" -"안통탄" -"괜히통탄했" -filter:retweets',
            '"한숨짐" OR "한숨지음" -"안한숨" -filter:retweets',
            '"한숨지었다" OR "한숨지었네" OR "한숨지었어" OR "한숨지었음" OR "한숨지었습니다" -"안한숨지었" -"괜히한숨지었" -filter:retweets',
            '"한탄한다" OR "한탄해" OR "한탄함" OR "한탄합니다" -"안한탄" -filter:retweets',
            '"한탄했다" OR "한탄했네" OR "한탄했어" OR "한탄했음" OR "한탄했습니다" -"안한탄" -"괜히한탄했" -filter:retweets',
            '"허무하다" OR "허무하네" OR "허무하군" OR "허무해" OR "허무함" OR "허무합니다" -"안허무" -filter:retweets',
            '"허무했다" OR "허무했네" OR "허무했어" OR "허무했음" OR "허무했습니다" -"안허무" -"괜히허무했" -filter:retweets',
            '"허전하다" OR "허전하네" OR "허전하군" OR "허전해" OR "허전함" OR "허전합니다" -"안허전" -filter:retweets',
            '"허탈하다" OR "허탈하네" OR "허탈하군" OR "허탈해" OR "허탈함" OR "허탈합니다" -"안허탈" -filter:retweets',
            '"허탈했다" OR "허탈했네" OR "허탈했어" OR "허탈했음" OR "허탈했습니다" -"안허탈" -"괜히허탈했" -filter:retweets',
            '"후회한다" OR "후회하네" OR "후회해" OR "후회함" OR "후회합니다" -"안후회" -filter:retweets',
            '"후회했다" OR "후회했네" OR "후회했어" OR "후회했음" OR "후회했습니다" -"안후회" -"괜히후회했" -filter:retweets',
            '"후회된다" OR "후회되네" OR "후회돼" OR "후회됨" OR "후회됍니다" -"안후회" -filter:retweets',
            '"후회됐다" OR "후회됐네" OR "후회됐어" OR "후회됐음" OR "후회됐습니다" -"안후회" -"괜히후회됐" -filter:retweets',
            ]

file = open("Sad.txt", 'a', -1, "utf-8")

lst = []

for keyword in keywords:
    cursor = tweepy.Cursor(api.search, 
                           q=keyword,
                           since='2018-01-01',
                           count=100,
                           geocode=location)
    for i, tweet in enumerate(cursor.items()):
        if not tweet.truncated:
            lst.append(tweet_processing(tweet.text))
            
set_lst = list(set(lst))
dataStr = '\n'.join(set_lst)

file.write(dataStr)

file.close()