from myConfig import readFileConfig,writeFileConfig

s = "Hola Mariano, como estas?"
writeFileConfig("myConfig.txt",s)
readFileConfig("myConfig.txt")
s = "Bien y vos?"
writeFileConfig("myConfig.txt",s)
s = "Bien, gracias a Dios"
writeFileConfig("myConfig.txt",s)
readFileConfig("myConfig.txt")