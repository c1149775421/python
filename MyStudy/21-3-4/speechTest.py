import speech
while True:
    print("开始说话：")
    say=speech.input()
    speech.say("you said:"+say)
    print("说话结束!")
    print()
    if say == "你好":
        speech.say("How are you?")
    elif say == "好":
        speech.say("对话结束")
        break;
        
