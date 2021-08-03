async def parse(code, ctx, bot, currentValue=ord("0"), varis={"?":"1"}):
    # Copyright (c) UCYT5040
    # minlang - A minimal language
    output = ""
    outputNext = False
    getNext = False
    setNext = False
    valNext = False
    appendNext = False
    getLoopAmount = False
    inLoop = False
    loopCode = ""
    runMoreTimes = 0
    for i in code:
        if valNext:
            currentValue = ord(i)
            valNext = False
            continue
        if appendNext:
            currentValue += ord(i)
            appendNext = False
            continue
        if getNext:
            currentValue = ord(varis[i])
            getNext = False
            continue
        if outputNext:
            output += chr(i)
            outputNext = False
            continue
        if setNext:
            varis[i] = chr(currentValue)
            setNext = False
            continue
        dontDoThis = False
        if inLoop:
            print("loop run")
            if i == ")":
                print("true")
                inLoop = False
                dontDoThis = True
            if not dontDoThis:
                loopCode += i
                continue
        if getLoopAmount:
            runMoreTimes = int(i)
            getLoopAmount = False
            inLoop = True
        while runMoreTimes > 0:
            if not inLoop:
                runMoreTimes -= 1
                output += await parse(loopCode, ctx, bot, currentValue, varis)
            else: break

        if i == "e": # Sets the current value to the next character
            valNext = True
        if i == "a": # Adds the next character to the current value
            appendNext = True
        if i == "p": # Print current value
            output += chr(currentValue)
        if i == "g": # Get the value of a variable
            getNext = True
        if i == "v": # Set a variable
            setNext = True
        if i == "(":
            getLoopAmount = True
        if i == "-":
            currentValue -= 1
        if i == "+":
            currentValue += 1
        if i == "i":
            def check(m):
                return ctx.message.author == m.author and ctx.channel == m.channel
            await ctx.send("Enter a single char for input.")
            msg = await bot.wait_for("message", timeout=60, check=check)
            currentValue = ord(msg.content[0])
    return output
