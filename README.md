# wowhead_parse
This little script can parse spells from wowhead | Этот маленький скрипт может парсить умения с WoWhead
Also you can get all info, if you will read file by line with IDs 0-50000 or 100000-200000
After parse you get lines like this:

"Просто царапина£Нет£Мгновенное действие£0 метров £ÅДает способность \"Просто царапина\":\n\n\nВо время действия \"Танца клинков\" вы получаете на 20% меньше физического урона. Вероятность получить критический урон от атак ближнего боя снижается на 6%, уровень угрозы от любых действий значительно повышается, а способность \"Ложный выпад\" заменяется на \"Издевку\", которая провоцирует цель атаковать вас.\n\n\nПровоцирует цель, заставляя ее атаковать вас. Не действует, если вы уже сражаетесь с целью.", --400039
"Держать удар£Нет£Мгновенное действие£0 метров £ÅДает способность \"Держать удар\":\n\n\nПри каждом уклонении или парировании ваш запас здоровья увеличивается на 6%. Суммируется до 5 раз.", --400040
"Гравировка нагрудника \"Смертельное варево\"£Нет£3 сек.£0 метров £ÅВыгравировать на нагруднике или мантии руну \"Смертельное варево\":\n\n\nУлучшает ваши яды несколькими эффектами:\n\nПоражая цель любым другим ядом, вы также отравляете ее \"Смертельным ядом\".\n\nЕсли на вашем оружии нет яда, оно может поразить цель \"Быстродействующим ядом\", словно он был нанесен на оружие.\n\nУрон от \"Смертельного яда\" и \"Быстродействующего яда\" теперь увеличивается в зависимости от вашей силы атаки.", --400080
"Гравировка поножей \"Промеж глаз\"£Нет£3 сек.£0 метров £ÅВыгравировать на поножах руну \"Промеж глаз\":\n\n\nБыстрый завершающий прием, наносящий урон за каждый прием в серии с бонусом за силу атаки и оглушающий цель:\n\n   1 прием: [53 / 100 * ( + )]-[81 / 100 * ( + )] ед. урона, оглушение на 1 сек.\n   2 приема: [53 / 100 * ( +* 2)]-[81 / 100 * ( +* 2)] ед. урона, оглушение на 2 сек.\n   3 приема: [53 / 100 * ( +* 3)]-[81 / 100 * ( +* 3)] ед. урона, оглушение на 3 сек.\n   4 приема: [53 / 100 * ( +* 4)]-[81 / 100 * ( +* 4)] ед. урона, оглушение на 4 сек.\n   5 приемов: [53 / 100 * ( +* 5)]-[81 / 100 * ( +* 5)] ед. урона, оглушение на 5 сек.\n\nОбщее время восстановления с \"Ударом по почкам\".", --400081
