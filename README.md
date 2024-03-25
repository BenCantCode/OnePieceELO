# One Piece 1v1 ELO

I calculated the ELO of every One Piece character. Take these results with a grain of salt, as the dataset may not be accurate, and even if it was, the ratings would still be very biased.

The 1v1 dataset was generated by taking the "Long Summary" for each One Piece chapter from the One Piece Wiki and grouping them into their respective arcs. These combined summaries, which can be found in `summaries/`, were then manually fed to Claude 3 Opus with the following prompt:

```
Create a JSON-formatted chronological list of every 1-on-1 battle in the (XYZ) Saga of One Piece.

Use the following format:

{"a": "first_character_lower_name", "b": "second_character_lower_name", "winner": "a"|"b"|"draw"}
```

The results were then added to `results.json`, with some manual fixes if Claude got the format wrong or added a group battle. The results haven't been otherwise been checked for accuracy.

After finding the results, a separate Python script (`elo.py`) was used to calculate the ratings.

## Results
1. luffy 1699.8058514970896 
1. zoro 1636.861486813061 
1. sanji 1620.6333683369073 
1. chopper 1584.6660070449905 
1. nami 1570.381113834543 
1. franky 1568.2348022679878 
1. blackbeard 1550.6943715115083 
1. jinbe 1550.2625702844568 
1. robin 1545.3371189137822 
1. mihawk 1538.285852778131 
1. enel 1537.1670831590416 
1. usopp 1531.0518834361408 
1. whitebeard 1529.5834312747097 
1. kizaru 1529.2149072304799 
1. magellan 1522.998263919659 
1. killer 1522.1354612166426 
1. judge 1520.6975480736915 
1. aokiji 1520.4571920180667 
1. senor pink 1519.3614492212907 
1. shanks 1516.7378650066732 
1. onigumo 1516.0125225388658 
1. hancock 1516.0 
1. pekoms 1516.0 
1. sabo 1516.0 
1. sai 1516.0 
1. bartolomeo 1516.0 
1. cavendish 1516.0 
1. kyros 1516.0 
1. inuarashi 1516.0 
1. nekomamushi 1516.0 
1. raizo 1516.0 
1. kikunojo 1516.0 
1. denjiro 1516.0 
1. yamato 1515.263693206478 
1. stussy 1515.213820167356 
1. big mom 1515.1996017700872 
1. garp 1506.2114301435383 
1. doflamingo 1505.4684941137157 
1. daifuku 1503.2758967688853 
1. jabra 1503.1131206431257 
1. sengoku 1501.780923969926 
1. wyper 1500.9173651890753 
1. gin 1500.736306793522 
1. shura 1500.736306793522 
1. ace 1500.0 
1. ivankov 1500.0 
1. kuma 1500.0 
1. pedro 1500.0 
1. tamago 1500.0 
1. kuzan 1499.5048192564873 
1. gan fall 1499.363724473774 
1. kid 1499.296043123496 
1. brook 1499.263693206478 
1. carrot 1499.263693206478 
1. drake 1499.263693206478 
1. kaku 1495.223624294801 
1. kaidou 1492.761525276002 
1. katakuri 1491.7639432656963 
1. cracker 1491.0014556168585 
1. gecko moria 1490.6458358355542 
1. pica 1490.0427887724318 
1. blueno 1489.8715954394374 
1. vander decken ix 1489.6923811444728 
1. hyouzou 1489.6287563268686 
1. king 1489.4854250035933 
1. foxy 1489.4464280435966 
1. surume 1489.255543015071 
1. s-shark 1488.8827496257566 
1. koby 1488.777789905284 
1. ryuma 1488.7180598386703 
1. yonji 1488.1960012600812 
1. kumadori 1488.0436416053567 
1. crocodile 1487.89739119338 
1. oven 1487.8734087793794 
1. queen 1487.7328324149778 
1. braham 1487.6853901385534 
1. dosun 1487.2660610777991 
1. ohm 1487.119097825516 
1. absalom 1487.094396251158 
1. ikaros much 1486.7748844007428 
1. arlong 1486.7238645358739 
1. hogback 1486.673580567152 
1. mr. 1 1486.5175552812955 
1. sasaki 1486.499982044743 
1. tararan 1486.152385829282 
1. buchi 1486.0982942088476 
1. don krieg 1486.0982942088476 
1. satori 1486.0679457412398 
1. kalifa 1486.003251969204 
1. hatchan 1485.879660946095 
1. wanze 1485.8518880497877 
1. marco 1485.6748787312247 
1. who's-who 1485.64787313675 
1. fukurou 1485.49308752385 
1. akainu 1485.4792958087392 
1. kuro 1485.4358728782763 
1. sham 1485.4358728782763 
1. black maria 1485.4123810052665 
1. mr. 2 1485.4037778232891 
1. gedatsu 1485.374732743402 
1. nero 1484.7966446868822 
1. john giant 1484.7820985594142 
1. cabaji 1484.736306793522 
1. hotori 1484.736306793522 
1. apoo 1484.736306793522 
1. daruma 1484.7261040949943 
1. kuroobi 1484.7024671725246 
1. hawkins 1484.2961529500892 
1. sentomaru 1484.2594044435564 
1. jozu 1484.215156636942 
1. alvida 1484.0 
1. morgan 1484.0 
1. pearl 1484.0 
1. chew 1484.0 
1. miss doublefinger 1484.0 
1. yama 1484.0 
1. smoker 1484.0 
1. moria 1484.0 
1. zeo 1484.0 
1. caribou 1484.0 
1. jesus burgess 1484.0 
1. lao g 1484.0 
1. gladius 1484.0 
1. dellinger 1484.0 
1. diamante 1484.0 
1. randolph 1484.0 
1. jack 1484.0 
1. perospero 1484.0 
1. fukurokuju 1484.0 
1. kanjuro 1484.0 
1. orochi 1484.0 
1. perona 1483.989282385175 
1. shiryu 1483.5276023197505 
1. sogeking 1483.378216372508 
1. hody jones 1479.4995997700082 
1. bellamy 1478.6025960594247 
1. rob lucci 1475.2007862165924 
1. hammond 1474.0407426103538 
1. wadatsumi 1473.2138046742416 
1. law 1471.8337876018995 
1. ulti 1471.345160315607 
1. miss merry christmas 1470.807676875899 
1. buggy 1470.5409216239211 
1. mr. 4 1469.4387739660467 
1. kotori 1469.3358416109802

## Significance

The plot of One Piece closely follows the Straw Hat Pirates, so their ELO is significantly inflated. Additionally, there are almost certainly errors caused by the non-deterministic AI processing step. As a result, these ratings are effectively meaningless (though I am a fan of Chopper soloing Blackbeard).

...still more logical than everything on /r/OnePiecePowerScaling though.

## Running

Grab the One Piece Wiki backup from https://onepiece.fandom.com/wiki/Special:Statistics, and then extract it into a file called `onepiece_pages_current.xml`. Drop that in this folder, then run `extract.py`. That will generate a list of summaries in the summaries folder. Throw each of those into your favorite AI tool (make sure it's got a long context length) and manually combine the responses into `battles.json`. Afterwards, run `elo.py` to generate the results.

## License

The generated summaries (not included) are taken from the [One Piece Wiki](https://onepiece.fandom.com/wiki/One_Piece_Wiki), which is available under the CC-BY-SA license.

The code in this repository is available under the WTFPL.
