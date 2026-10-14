# Zhu Xian (Jade Dynasty) Burmese Translation Repo (诛仙 / ကျူးရှန်း)

ဒီ repo သည် တရုတ်ဂန္ထဝင် Classical Xianxia (古典仙侠) ဝတ္ထုကြီးဖြစ်သော **Zhu Xian (Jade Dynasty - 诛仙)** ကို **English → Burmese** ဘာသာပြန်ဆိုရန်အတွက် တည်ဆောက်ထားသော project repository ဖြစ်ပါသည်။

---

## Novel Overview (ဝတ္တုအကျဉ်းချုပ်)

**Zhu Xian (诛仙 — ကျူးရှန်း / Jade Dynasty)** သည် နာမည်ကျော် စာရေးဆရာ **Xiao Ding (萧鼎 — ရှောင်းတိန့်)** ရေးသားခဲ့သော ရှေးရိုးမသေမျိုး တာအိုကျင့်ကြံခြင်း ဂန္ထဝင်လက်ရာမွန်ကြီး ဖြစ်ပါသည်။ 

၎င်းကို တရုတ်စာပေလောကတွင် **"Three Great Online Wonders" (网络三大奇书)** ထဲမှ တစ်ခုအဖြစ်လည်းကောင်း၊ ကျင်းယုံ (Jin Yong) နောက်ပိုင်း အကောင်းဆုံး ဝူရှန်း/ရှန်းရှ ဝတ္ထုအဖြစ် **"Post-Jin Yong Wuxia Bible" (后金庸武侠圣经)** အဖြစ်လည်းကောင်း တင်စားခေါ်ဝေါ်ကြပါသည်။

### ဇာတ်လမ်းအကျဉ်း:
Caomiao Village (မြက်ကျောင်းရွာ) တွင် တစ်ရွာလုံး အစုလိုက်အပြုံလိုက် ရက်စက်စွာ သတ်ဖြတ်ခံရမှုမှ လွတ်မြောက်လာသော သာမန်ရိုးသားသည့် ကောင်လေး Zhang Xiaofan (ကျန်းရှောင်ဖန်) သည် Qingyun Sect (ချင်ယွင်ဂိုဏ်း) ၏ Dazhu Peak (ဝါးကြီးထွတ်) သို့ ရောက်ရှိပြီး တာအိုကျင့်စဉ်ကို စတင်သင်ယူခဲ့သည်။ သူ မသိလိုက်ဘဲ ရရှိခဲ့သော ဗုဒ္ဓဘာသာကျင့်စဉ် (Great Brahma Prajna) နှင့် မာရ်နတ်ရတနာ (Blood Dripping Pearl) တို့ကြောင့် သူ၏ ကံကြမ္မာမှာ မုန်တိုင်းထန်ခဲ့ရသည်။

မာရ်နတ်ဘုရင်ဂိုဏ်းချုပ်၏ သမီးတော် Bi Yao (ပိယောင်) နှင့် ချစ်ကြိုးသွယ်မိခဲ့သော်လည်း တရားနှင့် မာရ်နတ်အကြား သွေးစွန်းသော စစ်ပွဲကြီးတွင် ပိယောင်သည် ကျန်းရှောင်ဖန်ကို ကယ်တင်ရန် မိမိ၏ ခန္ဓာနှင့် ဝိညာဉ်ကို မာရ်နတ်သွေးကျိန်စာ (Chiqing Curse) ဖြင့် စတေးခဲ့သည်။ ဤကြေကွဲဖွယ်ဖြစ်ရပ်ကြောင့် ကျန်းရှောင်ဖန်သည် ဂိုဏ်းမှ ထွက်ခွာကာ မာရ်နတ်ဘုရင်ဂိုဏ်း၏ ဒုတိယခေါင်းဆောင် "သွေးသခင်လေး ကွေ့လီ" (Gui Li) အဖြစ် ၁၀ နှစ်တိုင် ပိယောင်ကို နိုးထစေရန် နည်းလမ်းရှာဖွေရင်း သွေးစွန်းသော လောကဓံကို ဖြတ်သန်းခဲ့ရသည်။

ဝတ္ထု၏ အဓိက ဒဿနမှာ တာအိုကျမ်းလာ **"天地不仁，以万物为刍狗"** (*ကောင်းကင်နှင့် မြေကြီးသည် ဘက်လိုက်ခြင်း မရှိ၊ သက်ရှိခပ်သိမ်းကို မြက်ကောက်ရိုးခွေးရုပ်များကဲ့သို့သာ သဘောထား၏*) ဟူသည့်အတိုင်း တရားသောသူတို့သည် အမြဲဖြောင့်မတ်သလော၊ မာရ်နတ်သမားတို့သည် အမြဲယုတ်မာသလော ဟူသော ကံကြမ္မာ၊ အချစ်နှင့် သစ္စာတရား၏ နက်နဲမှုကို အနုပညာဆန်စွာ ရေးဖွဲ့ထားခြင်း ဖြစ်ပါသည်။

---

## Repository Structure (ဖိုင်တွဲစနစ်)

```text
d:\zhuxian\
├── .github/workflows/      # GitHub Actions CI/CD (GitHub Pages auto-deploy)
├── reader/                 # Static web reader (PWA, offline cache, mobile-friendly)
├── eng/                    # English source chapters (0001.md – 0264.md)
├── burmese/                # Burmese translated chapters (0001.md – 0264.md)
├── ref.md                  # Comprehensive translation reference bible
├── SKILL.md                # AI Agent translation skill & system instructions
├── track.md                # Translation progress tracker (Single Source of Truth)
├── README.md               # Repository overview and documentation
├── fetch_all.py            # Python scraper used to fetch English chapters
└── .gitignore              # Git ignore rules
```

- **`reader/`**: Markdown အခန်းများကို browser တွင် အလွယ်တကူ ဖတ်ရှုနိုင်သော Modern Web Reader (PWA / Offline cache အထောက်အပံ့ပါဝင်သည်)။
- **`.github/workflows/deploy-pages.yml`**: Git push ပြုလုပ်လိုက်တိုင်း GitHub Pages သို့ Reader website ကို အလိုအလျောက် build လုပ်ပြီး deploy ပေးမည့် GitHub Actions Pipeline။
- **`eng/`**: အင်္ဂလိပ် မူရင်း အခန်းများ (စုစုပေါင်း ၂၆၄ ခန်း)။ ဖိုင်အမည်များကို 4-digit zero-padded စနစ် (`0001.md` = Prologue, `0002.md` = Chapter 1 မှစ၍ `0264.md` အထိ) ဖြင့် သိမ်းဆည်းထားသည်။
- **`burmese/`**: မြန်မာဘာသာပြန် အခန်းများ။ မူရင်း English ဖိုင်အမည်များနှင့် တစ်ထပ်တည်း တူညီစွာ (`burmese/0001.md`, `burmese/0002.md` စသဖြင့်) သိမ်းဆည်းမည်။
- **`ref.md`**: ဘာသာပြန်ရာတွင် အခြေခံရမည့် တရားဝင် အကိုးအကားကျမ်း (ဝတ္ထုသမိုင်း၊ ဇာတ်ကောင် ၃၀ ကျော်၊ ဂိုဏ်းများ၊ ရတနာများ၊ နတ်သားရဲကြီးများ၊ ကျင့်စဉ်အဆင့်များနှင့် တရားဝင် မြန်မာပြန် ဝေါဟာရများ)။
- **`SKILL.md`**: ဘာသာပြန် AI Agent လိုက်နာရမည့် ဘာသာစကားလေသံ၊ စည်းမျဉ်းများ၊ ဇာတ်ကောင်အလိုက် စကားပြောဟန်များနှင့် အသုံးအနှုန်းဇယားများ။
- **`track.md`**: ဘာသာပြန်ပြီးစီးမှု အခြေအနေ (Progress tracker)။

---

## Translation Guidelines & Instructions (ဘာသာပြန် လမ်းညွှန်ချက် အကျဉ်း)

ဘာသာပြန်ဆိုရာတွင် အောက်ပါ official guide နှစ်ခုကို မဖြစ်မနေ လိုက်နာရမည်-
1. [`d:\zhuxian\ref.md`](ref.md)
2. [`d:\zhuxian\SKILL.md`](SKILL.md)

### အဓိက စည်းမျဉ်းများ:
1. **ဂိုဏ်းနှင့် ကျင့်စဉ်ဝေါဟာရများ (Strict Glossary):** Taiji Xuanqing Dao (Jade Pure, Upper Pure, Grand Pure), Great Brahma Prajna စသည့် ကျင့်စဉ်များနှင့် ဂိုဏ်းခွဲများကို `ref.md` ဇယားများအတိုင်းသာ တသမတ်တည်း သုံးရမည်။
2. **Classical Xianxia စာပေဟန်:** အဆင့်တက် ဂိမ်းဆန်ဆန် ဝတ္ထုမျိုး မဟုတ်ဘဲ စိတ်ခံစားချက်၊ ဒဿနနှင့် ရှေးရိုးရိုးရာ ကဗျာဆန်မှုတို့ကို ပေါ်လွင်စေရန် သုခုမစာပေဆန်သော မြန်မာစကားပြေဖြင့် ပြန်ဆိုရမည်။
3. **ဇာတ်ကောင်အလိုက် လေသံထိန်းသိမ်းခြင်း (Character Voice Consistency):**
   - **Zhang Xiaofan (ငယ်စဉ်):** ရိုးသားယဉ်ကျေးသော `"ကျွန်တော်"` သုံးစွဲပုံ။
   - **Gui Li (ကွေ့လီ / သွေးသခင်လေး):** မာရ်နတ်လောကတွင် ကျင်လည်သဖြင့် အေးစက်တည်ကြည်သော `"ငါ/ကျုပ်"` သုံးစွဲပုံ၊ ဆရာသမားများနှင့် တွေ့ဆုံချိန်တွင် ရိုသေကြေကွဲသော အသံ။
   - **Bi Yao (ပိယောင်):** ရဲရင့်ပြတ်သားပြီး ကျန်းရှောင်ဖန်အပေါ် စနောက်ချစ်ခင်ကာ အသက်စွန့်ဝံ့သော မေတ္တာလေသံ။
   - **Lu Xueqi (လုရွှယ်ချီ):** တည်ကြည်အေးစက်သော ကောင်းကင်နတ်သမီးဟန်၊ စကားနည်းသော်လည်း ကျန်းရှောင်ဖန်အတွက် အဆုံးမဲ့ငရဲထိ လိုက်ရဲသော လေသံ။
4. **ဂိုဏ်းအမြင် သုံးနှုန်းပုံ (Factional Perspectives):**
   - မာရ်နတ်ဂိုဏ်းဘက်မှ ပြောဆိုရာတွင် **"သန့်ရှင်းသော သာသနာတော်" (Holy Religion / 圣教)**။
   - တရားဓမ္မဂိုဏ်းဘက်မှ ပြောဆိုရာတွင် **"မာရ်နတ်မိစ္ဆာဂိုဏ်း" (Demonic Cult / 魔教)**။
5. **Output Format:**
   - ဖိုင်လမ်းကြောင်း: `burmese/XXXX.md` (ဥပမာ- `burmese/0001.md`, `burmese/0002.md`)
   - ခေါင်းစဉ်: `# [မြန်မာခေါင်းစဉ်] ([English Title] / [Chinese Title])`
6. **Chunking Rule (User Rule):**
   - အခန်းတစ်ခန်းလုံးကို အပြည့်အစုံ ဦးစွာ ပြန်ဆိုရမည်။ Token limit error ကြုံတွေ့မှသာ Part 1, Part 2 ခွဲ၍ ပြန်ဆိုရမည်။

---

## Web Reader (ဝဘ်ဆိုဒ်ဖြင့် ဖတ်ရှုခြင်း)

ဤ repository တွင် အခန်းများကို သန့်ရှင်းသပ်ရပ်စွာ ဖတ်ရှုနိုင်သော Modern PWA Web Reader ပါဝင်ပါသည်။

### ၁။ စက်တွင်း (Locally) ဖွင့်လှစ်ဖတ်ရှုရန်:
```powershell
powershell -ExecutionPolicy Bypass -File .\reader\run_reader.ps1
```
ပြီးနောက် Browser တွင် `http://localhost:8000/reader/` သို့ ဝင်ရောက်ဖတ်ရှုနိုင်ပါသည်။

### ၂။ အခန်းသစ်များ ထည့်သွင်းပြီးပါက Index Update ပြုလုပ်ရန်:
```powershell
python .\reader\generate_manifest.py
```

---

## GitHub Actions & GitHub Pages Deployment

- Git ၏ `main` branch သို့ အခန်းသစ်များ push ပြုလုပ်လိုက်တိုင်း [`.github/workflows/deploy-pages.yml`](.github/workflows/deploy-pages.yml) သည် Reader website နှင့် စာမူများကို အလိုအလျောက် build ပြုလုပ်ပြီး **GitHub Pages** ပေါ်သို့ တိုက်ရိုက် deploy လုပ်ပေးသွားမည် ဖြစ်ပါသည်။
- အသုံးပြုသူသည် GitHub Repository Settings > Pages တွင် Source ကို **GitHub Actions** အဖြစ် ရွေးချယ်ပေးထားရုံဖြင့် မည်သည့် server မျှ မလိုဘဲ အခမဲ့ အွန်လိုင်းမှ ဖတ်ရှုနိုင်မည် ဖြစ်ပါသည်။

---

## Progress Tracking

လုပ်ငန်းပြီးစီးမှု အခြေအနေများကို [track.md](track.md) တွင် အမြဲမပြတ် update ပြုလုပ်သွားမည် ဖြစ်ပါသည်။
