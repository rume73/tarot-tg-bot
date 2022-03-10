info_card_dict = {
    0: 'Шут.\nЧто-то новое, интересное хочет войти в Вашу жизнь!\nПринимайте!\nОткройтесь, доверьтесь миру! Получайте удовольствие от каждой прожитой минуты.',
    1: 'Маг.\nПора Действовать! У Вас получится!',
    2: 'Жрица.\nСегодня только наблюдайте, действовать еще рано.',
    3: 'Императрица.\nЕсть все основания радоваться! Императрица предвещает насыщенное время, богатое, дающими удовлетворение, событиями!\nЛюбое дело, под её подкровительством процветает: и в любви, и в бизнесе, и в финансах!',
    4: 'Император.\nГлавное значение этой арканы - реализация замыслов. Стабильность, надежность, покровительство, помощь.\nПрисутствие этой карты говорит нам о прочности и постоянстве. И если в Вашей жизни сейчас кавардак - знайте, постепенно все придет к порядку.',
    5: 'Жрец.\nДоверие, вера - основные ценности сегодня! Доверяйте миру, верьте в себя и в то, что помощь придет. И правила! Соблюдайте правила! Все правила! И будет Вам счастье!',
    6: 'Влюбленные.\nСозданный сегодня союз будет долговечный и удобный.',
    7: 'Колесница.\nПрорыв, движение к цели! Путь свободен! Вы полны решимости и ничто не стоит на пути к успеху. Действуйте! У Вас получится!',
    8: 'Справедливость.\nБудь внимателен ко всем официальным документам. Что посеешь, то и пожнешь.',
    9: 'Отшельник.\nЗахочется уединиться, чтобы обдумать происходящее.',
    10: 'Фортуна.\nЭто карта перемен. Как правило, удачных. Колесо Фортуны говорит, что в жизни пошла динамика, непредсказуемый поворот событий. И, чтобы сегодня ни случилось, знайте - это к добру!',
    11: 'Сила.\nСегодня любые дела Вам по силам.',
    12: 'Повешенный.\nСитуация \"зависания\". В делах задержки, перед Вами резко выстраиваются очереди, на дорогах сплошные пробки. И Интернет может зависнуть. Принимайте все как есть, успокойтесь. Сегодня так...',
    13: 'Смерть.\nС чем устаревшим придется расстаться, чтобы поместить на его место новое. Не бойся что-то менять.',
    14: 'Умеренность.\nМягкая спокойная гармония. Дела продвигаются неторопливо, ни и без особых препятствий. Сглажены \"острые углы\" Мирное безмятежное существование. Этот аркан сулит Вам смягчение разногласий и снижение напряжённости',
    15: 'Дьявол.\nОн частенько пытается ввести нас в зависимость от ситуации, вывести нас на эмоции и сбить с истинного пути. Не позволяйте эмоциям и страхам управлять Вами.',
    16: 'Башня.\nСегодня будьте осторожны. Берегите себя и близких',
    17: 'Звезда.\nВдохновение, окрыленность, воодушевление.\nВы готовы слушать голос души. Появляются новые цели. Хочется мечтать. Состояние, когда вера несет силу, и изнутри идёт спокойствие и умиротвореность.',
    18: 'Луна.\nВсе не так, как кажется. И грань между интуицией и воображением сейчас размыта как никогда.\nНе надо пускаться в приключения. Не испытывайте себя на прочность. Сейчас стоит проявить осторожность.',
    19: 'Солнце.\nСчастье, радость, исполнение желаний',
    20: 'Суд.\nОбновление высвобождение скрытых талантов. Счастье, чувство свободы. Открывается новый смысл, новый вид восприятия вещей. И возможно именно сегодня в Вашей жизни завершится кризис и начнётся подъём.',
    21: 'Мир.\nЭто символ успеха, исполнение желаний достижения целей.\n Покой души,наслождение жизнью, радость и вдохновение - вот настроение дня.\nИ есть понимание: все что Вы делаете - правильно!',
    22: 'Туз жезлов.\nДень благоприятен для начала чего-то нового. Удачный день.',
    23: 'Двойка жезлов.\nДень принятия решения. Посмотрите на ситуацию со всех сторон.',
    24: 'Тройка жезлов.\nРост, стабильность, успех. Это касается и отношений, и карьеры, и духовного роста\nВаши идеи запускаются \"в производство\". Движение пошло. И 3 жезлов говорит, что все будет хорошо.',
    25: 'Четверка жезлов.\nСтабильность и изобилие, добрый и счастливый день.',
    26: 'Пятерка жезлов.\nКонкуренция!\nИспользуйте этот \"турнир\", чтобы улучшить свои способности. Используйте конкурирующие энергии, чтобы обогатить свой опыт. Позвольте чувства вызова помочь Вам выйти за пределы Ваших собственных ограничений.',
    27: 'Шестерка жезлов.\nПобеда, успех. Добрые вести',
    28: 'Семерка жезлов.\nСамоутверждение!\nВозможны нападки, попытки навредить Вам, покушаение на то, что принадлежит Вам. Придется отстаивать себя и свои границы. Приятная новость в том, что у Вас есть все шансы одержать победу.',
    29: 'Восьмерка жезлов.\nОбстоятельства таковы, что желаемое событие начинает разворачиваться! Все в движении!\nПроизойдёт что-то важное и нужное в результате удачного стечения обстоятельств. Или Вам в голову придёт неожиданное решение проблем. У вас откроется второе дыхание. Коротко говоря: \"куй железо, пока горячо\". Сейчас удача на Вашей стороне!',
    30: 'Девятка жезлов.\nЕсли нет желания вступить в контакт с чужими людьми - послушайте себя.',
    31: 'Десятка жезлов.\nНе взваливайте на себя лишний груз. Не стоит работать за себя и за того парня',
    32: 'Паж жезлов.\nПриятная атмосфера в семье, дома и в кругу друзей.',
    33: 'Рыцарь жезлов.\nЖизнь бурлит! И тебе это нравится!',
    34: 'Королева жезлов.\nЛидерство, гордость и желание действовать - вот настроение дня. В конкуренции Вы имеете преимущество. Вы зажигательны. Вы привлекательны. С Вами интересно - это факт.',
    35: 'Король жезлов.\nВаши усилия приведут к успеху.',
    36: 'Туз кубков.\nОдна из самых благоприятных карт. Она указывает на прекрасный шанс и говорит о благоприятных перспективах.\nИ далее об исполнении желания. Хватайтесь за шанс!',
    37: 'Двойка кубков.\nЭта карта говорит о взаимной любви! Или о том, что вы готовы встретить свою любовь!\nИ ещё сегодня Вас будет сопровождать прекрасное настроение: душа поёт, красота замечается даже там, где Вы её раньше и не видели! Вы сегодня счастливы, добры и привлекательны!',
    38: 'Тройка кубков.\nЭта карта несет простые радости, которые помогают ощутить беззаботность и счастье.\nСегодня с Вами может случиться встреча, веселая вечеринка и радостное наслождение происходящим!',
    39: 'Четверка кубков.\nПроснитесь!\nЕсли Вы будете печалиться и крутить в голове мысли об обиде или потере - есть шанс упустить что-то очень хорошее, что приготовила для Вас жизнь!',
    40: 'Пятерка кубков.\nРазочарование, печаль. Хорошо, что эта карта только на день.',
    41: 'Шестерка кубков.\nРадость, благополучие. Приятные воспоминания.',
    42: 'Семерка кубков.\nКарта тумана, миражей. Под этой картой мы питаем себя иллюзиями. Обманываем себя надеждами - несбыточными. Строим планы.\nСегодня только мечтаем, но не планируем. Все серьезные намерения лучше перенести на завтра.',
    43: 'Восьмерка кубков.\nПереход от устаревшего к чему-то новому.',
    44: 'Девятка кубков.\nСчастье, успех, удовлетворение содеянным.',
    45: 'Десятка кубков.\nСчастье!\nЖизнерадостность, наслождение каждой минутой, эмоциональное удовлетворение!\nИ радость, радость, такая, душевная!',
    46: 'Паж кубков.\nПредвещает приятные переживания, свежие чувства, новые знакомства. Это так же может быть нечто новое в Ваших уже имеющихся отношениях: подарки, комплименты, признания в любви!\nВ любом случае, Паж чаш обещает наполненную радостную жизнь!',
    47: 'Рыцарь кубков.\nВестки любви. Любовь к Вам идёт!\nВ любом случае Рыцарь кубков обещает теплые взаимотношения, чувства, приятный эмоциональный подъем, приятные свидания, еще примерение.',
    48: 'Королева кубков.\nСостояние покоя, ожидания, задумчивость. Прислушивание к себе. Вообще, настроение приятное и карта говорит, что сегодня Вы будете чувствовать себя в безопасности и с доверием.',
    49: 'Король кубков.\nПолучишь мудрый совет и поддержку.',
    50: 'Туз мечей.\nРешение!\nВы полны решимости действовать. Вы знаете, что делать дальше. И Вы имеете достаточно силы воли, физической силы и знаний, чтобы справиться с поставленной задачей. У Вас получится!',
    51: 'Двойка мечей.\nПоявится потребность закрыться, погрузиться в себе, чтобы продумать план действийю Это нужно, чтобы сейчас не совершать ошибку и, по возможности, избежать конфликта. Успокоить свои эмоции.',
    52: 'Тройка мечей.\nБерегите свое сердце в прямом и переносном смысле. Возможные неприятные известия.',
    53: 'Четверка мечей.\nТо, что говорит твой разум, важнее, чем то, что говорит окружение. Сегодня так. Не навязывайся, не напрашивайся, будь один, защищай свое единение.',
    54: 'Пятерка мечей.\nНе вступайте в споры, не пытайтесь доказать. Сегодня лучше ничего не делать.',
    55: 'Шестерка мечей.\nВы стремитесь уйти от старого к новому. Новым может быть и отношение к текущему положению. Но, скорее всего, Вы стремитесь к лучшему, к переменам, к новым берегам. И у Вас получится. Возможно, Вы испытываете неуверенность, потому что неизвестность пугает. Не бойтесь - там хорошо!',
    56: 'Семерка мечей.\nПроявите хитрость и смекалку, но и сами не теряйте бдительность, чтобы Вас не обхитрили.',
    57: 'Восьмерка мечей.\nОщущение ограничений, трудностей, запретов. Сомнения и внутренние конфликты не дают нам сделать ни шагу к цели. Сегодня так. Хорошая новость: влияние 8 мечей временно.',
    58: 'Девятка мечей.\nСон разума порождает чудовище. Тревога, страх неудачи. Возможно Вы мучаете себя, воображение самое неприятное, что только может случиться. Если Вам выпала 9 мечей - это озночает, что большинство проблем выдуманы и в несколько разувеличены именно в Вашей голове.',
    59: 'Десятка мечей.\nДействия обречены на неудачу. Подумайте, как минимизировать потери. А лучше ничего сегодня не предпринимайте.',
    60: 'Паж мечей.\nИнтерес и любопытство. Желание \"пополнить шкатулку своих знаний\". Сегодня Вы хороший слушатель. Однако, вместе с этим, у Вас будет желание быть дерзким и острым на слово. Лучше в такое моменты сдержаться и переключиться на что-то хорошее.',
    61: 'Рыцарь мечей.\nДействуйте быстро, не задумываясь, чтобы не упустить момент.',
    62: 'Королева мечей.\nСегодня не стоит проявлять слишком бурно свои эмоции. День хороший.',
    63: 'Король мечей.\nОтбрось эмоции, возьми на вооружением ум, опытность, бесстрашие и активность! Тебе сегодня они пригодятся!',
    64: 'Туз пентаклей.\nДар материальной реальности: процветание, обилие ресурсов. Ощущение счастья! И счастье именно то, которое понимается в самом Земном смысле: стабильность, процветание, прекрасное самочувствие.',
    65: 'Двойка пентаклей.\nСегодня придется похлопотать, чтобы удержать равновесие, если выровнять свою \"лодку\". Возможно немного придётся понервничать. Но, при определенных усилиях, Вы справитесь с поставленными задачами.',
    66: 'Тройка пентаклей.\nНе старайся все сделать в одиночку, работа в коллективе приблизит реализацию проекта.',
    67: 'Четверка пентаклей.\nРассчетливость, тщательное планирование. Готовность действовать, чтобы достичь желаемой стабильности. Эта карта дает ощущение устойчивости. Но: так же и описание: что-то угрожает стабильности. Стремление оберегать свои ценности.',
    68: 'Пятерка пентаклей.\nСегодня лучше отказаться от необдуманных трат.',
    69: 'Шестерка пентаклей.\nГармоничное состояние. Сегодня Вы и великодушны, и благодарны.',
    70: 'Семерка пентаклей.\nВы все сделали правильно в саду своей жизни. Теперь Вы просто должны подогнать, как созреют плоды.',
    71: 'Восьмерка пентаклей.\nЛюбая работа настолько интересна, на сколько интересен ты сам! Сегодня Вы получите удовлетворение от применения своих талантов.',
    72: 'Девятка пентаклей.\nЭта карта сулит ситуацию, о которой в народе говорят: \"счастье привалило\"! Сегодня жизнь повернулась к Вам светлой стороной. Ждёт Вас сегодня удача. Возможно именно сегодня в Вашей жизни произойдёт поворот к лучшему.',
    73: 'Десятка пентаклей.\nЭта карта богатства стабильности, уверенности, полноты жизни. Сегодня Вас посетит ощущение покоя и счастья, чувство , что все что Вы делали сегодня приносит свои прекрасные плоды.',
    74: 'Паж пентаклей.\nПрактичность на первом месте. И возможно сегодня к Вам придёт идея в каком направлении двигаться дальше. И Вы будете готовы обучаться чему-то новому, потому что это новое пойдёт на пользу! А ещё эта карта предсказывает приятный отдых на природе, в ресторане, или даже Земные радости.',
    75: 'Рыцарь пентаклей.\nЭтот аркан призывает Вас заняться полезным делом. Ведь пусть к хорошим результатам прикладывается трудом и совершенствованием. А еще эта карта говорит о хороших возможностях, стабилизации и улучшении финансового пополнения. Так что действуйте.',
    76: 'Королева пентаклей.\nВаше материальное положение благополучно и стабильно.',
    77: 'Король пентаклей.\nСтабильная ситуация. Прочная основа для любых начинаний.'
    }

yes_no_dict = {
    0: 'Да',
    1: 'Да',
    2: 'Неизвестно',
    3: 'Да',
    4: 'Да',
    5: 'Да',
    6: 'Да',
    7: 'Да',
    8: 'Да',
    9: 'Да',
    10: 'Да',
    11: 'Да',
    12: 'Нет',
    13: 'Нет',
    14: 'Да',
    15: 'Нет',
    16: 'Нет',
    17: 'Да',
    18: 'Нет',
    19: 'Да',
    20: 'Да',
    21: 'Да',
    22: 'Да',
    23: 'Да',
    24: 'Да',
    25: 'Да',
    26: 'Да, если приложите усилия',
    27: 'Да',
    28: 'Да, если приложите усилия',
    29: 'Да',
    30: 'Нет',
    31: 'Нет',
    32: 'Да',
    33: 'Да',
    34: 'Да',
    35: 'Да',
    36: 'Да',
    37: 'Да',
    38: 'Да',
    39: 'Нет',
    40: 'Нет',
    41: 'Да',
    42: 'Нет',
    43: 'Нет',
    44: 'Да',
    45: 'Да',
    46: 'Да',
    47: 'Да',
    48: 'Да',
    49: 'Да',
    50: 'Да',
    51: 'Нет',
    52: 'Нет',
    53: 'Нет',
    54: 'Нет',
    55: 'Да',
    56: 'Нет',
    57: 'Нет',
    58: 'Нет',
    59: 'Нет',
    60: 'Нет',
    61: 'Нет',
    62: 'Да',
    63: 'Да',
    64: 'Да',
    65: 'Нейтрально',
    66: 'Да',
    67: 'Да',
    68: 'Нет',
    69: 'Да',
    70: 'Нет',
    71: 'Да',
    72: 'Да',
    73: 'Да',
    74: 'Да',
    75: 'Да',
    76: 'Да',
    77: 'Да'
    }
