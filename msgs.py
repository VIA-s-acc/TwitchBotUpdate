#EVENTCOG MSGS
USERINITMSG = "INSERT INTO users VALUES('{name}','{id}','{chnl}',{df})"
IDSELECTMSG = "SELECT user_id from users WHERE user_id = {ID} and channel_name = '{CHNL}'"
USERINFUPD = "UPDATE users SET message_count = message_count + {COUNT}  WHERE user_id = {ID}  and channel_name = '{CHNL}'"
USERUPDMSG = "=========Сообщение=========\nКанал <NAME:{CHNL}>\nСообщение От <NAME:{NAME}	id:{ID}>\nТекст "\
            "Сообщения <{MSG}>\nДата: {DATE} \nadd to db logs table\n===========================\n\n"
LOGSMSG = "INSERT INTO logs VALUES({ID},'{NAME}','{CHNL}','{MSG}','{DATE}')"



#SEARCHCOG MSGS
UAGNT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.3.823 Yowser/2.5 Safari/537.36"
WIKIERRMSG = 'В wikipedia не было найдено соотвествующей информации по запросу <{query}>.\nНиже даны ссылки ,которые могут помочь.\n'



#CHATCOMS MSGS
MSGCOUNTSEL = "SELECT message_count from users WHERE user_id = {ID} and channel_name = '{CHNL}'"
MSGCOUNTSEN = "{AUTHOR}, вы написали {CNT} сообщений на канале {CHNL}."
MSGCOUNTSENU = "{AUTHOR}, пользователь {USER} написал {CNT} сообщений на канале {CHNL}."



#LENMSGS
LEN10 = "{AUTHOR}, у вас {LNG} см, не отчаиваетесь(((."
LEN20 = "{AUTHOR}, у вас {LNG} см, +rep."
LEN30 = "{AUTHOR}, у вас {LNG} см, Вам ничего не мешает?"
LEN40 = "{AUTHOR}, у вас {LNG} см, как вы вообще живёте..."
LENV = "{AUTHOR}, эммм, какого фига у вас {LNG} см..."



#RANDMSGS
RQUOTERRMSG = "{AUTHOR} произошла ошибка | Цитат от {NAME} не было найдено."
RQUOTEGENERRMSG = "{AUTHOR}, произошел сбой при генерации цитаты | Информация : Не найдена цитата от {NAME} подходящей длины | ERRINFO: TIMEOUTERR."
RQUOTEMSGF = "РАНДОМНАЯ ЦИТАТА :    {TEXT} | Автор : {AUTHOR} | Книга : {BOOK}."
RQUOTEMSGS = "РАНДОМНАЯ ЦИТАТА :    {TEXT} | Автор : {AUTHOR}."



#WTHRMSGS
WURL = 'http://api.openweathermap.org/data/2.5/weather?q={LCT}&appid={AK}'
WERRMSG = "{AUTHOR}, Error 404"


#MRGEMSGS
SELUSF = "SELECT user1_id FROM marry WHERE user1_id = '{USRF}' AND channel_name = '{CHNL}'"
INMR = "{AUHTOR}, {USER} уже состоит в браке."
SELFM = "{AUTHOR}, выберите другого пользователя!"
MWAIT = '{AUTHOR}, пожалуйста подождите, запрос брака между {USRF} и {USRS} в обработке.'
USSELERR = "{AUTHOR}, выберете пользователя для предложения."
MRANSWMSG = "{AUTHOR}, ожидаем ответа от {USER} (овтет в виде сообщения <Да> для согласия, оно будет автоматически отклонено через 60 секунд)"
MRGNOT = "{AUTHOR}, вы не состоите в браке."
UMRGNOT = "{AUTHOR}, пользователь {USER} не состоит в браке."
SELUSS = "SELECT user2_id FROM marry WHERE user1_id = {USRF} AND channel_name = '{CHNL}'"
SELUSSN = "SELECT user2_name FROM marry WHERE user1_id = {USRF} AND channel_name = '{CHNL}'"
DELFMRS = "DELETE from marry where user1_id = {USRF} AND channel_name = '{CHNL}'"



#CustomCommandMsg
CCCHECK = "SELECT 1 FROM comms WHERE comm_name = '{COMM}' AND channel_name = '{CHNL}'"
CCCSEL = "SELECT comm_text FROM comms WHERE comm_name = '{COMM}' AND channel_name = '{CHNL}'"
CNERR = 'Название комманды должно быть 1 словом | your comm_name {comm_name}'
CODEERR = "Exception in code : {Exception}"
CCSYMERR = "В названии команды не должно быть символов из [,./*-+1234567890!@#$%`&()_:';~:]"
COMMSET = "INSERT OR REPLACE INTO comms VALUES('{CHNL}','{COMM}','{TXT}')"
COMMDEL = "DELETE FROM comms WHERE channel_name = '{CHNL}' AND comm_name = '{COMM}'"