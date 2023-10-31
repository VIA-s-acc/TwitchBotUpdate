#EVENTCOG MSGS
USERINITMSG = "INSERT INTO users VALUES('{name}','{id}','{chnl}',{df})"
IDSELECTMSG = "SELECT user_id from users WHERE user_id = {ID} and channel_name = '{CHNL}'"
USERINFUPD = "UPDATE users SET message_count = message_count + {COUNT}  WHERE user_id = {ID}  and channel_name = '{CHNL}'"
USERUPDMSG = "=========Сообщение=========\nКанал <NAME:{CHNL}>\nСообщение От <NAME:{NAME}	id:{ID}>\nТекст "\
            "Сообщения <{MSG}>\nДата: {DATE} \nadd to db logs table\n===========================\n\n"
LOGSMSG = "INSERT INTO logs VALUES({ID},'{NAME}','{CHNL}','{MSG}','{DATE}')"



#SEARCHCOG MSGS
UAGNT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.3.823 Yowser/2.5 Safari/537.36"