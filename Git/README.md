
### __Git ve Github - Terminal Üzerinde Git İşlemleri, Komut Açıklamaları ve Pull Request__

---

### Table of Contents

1. [Initialization & Local Repo Operations](#init)
2. [Branch (Dallanma)](#branch)
3. [Undoing in Git](#undoing)
4. [Pull Request - Open Source](#pr)

---

### 1. Initialization & Local Repo Operations <a name="init"></a>

> ``` git init ```

Bu komut ile lokalde bir klasör veya dizinde ___git initialization___ işlemi gerçekleştiriyorz. Bundan sonra diğer git komutlarını rahatlıkla çalıştırabiliriz.

Daha sonra github lokal cihaz ile github hesabınız arasında bağlantı sağlanması gerekmektedir. [Connecting to Github](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh)

> ``` git clone  repo link ```

Herhangi bir repoyu (pratik yapmak için tercihen kendinize ait bir repo) içinde bulunduğumuz dizine çekiyoruz.

Kodlar ya da proje dosyalarında bir değişiklik yaptıktan sonra bu değişiklikler güncellemeye hazır duruma getirilmelidir.

Değişiklik yapılmış dosyaları kontrol etmek için

> ``` git status ```

Bunları commit etmeye hazır hale getirmek için

> ``` git add .``` (tüm değişiklikler için .(nokta) ) - ( Sadece belirli değişiklileri commit sırasına almak için ise nokta yerine o dosyanın dizini örneğin sadece ReadME.md)

> ``` git commit -m “commit message” ```

Artık lokal üzerindeki adımlar tamamlandı, yapılan değişiklikler github server’larına aktarılmaya hazır.

 > ```git push -u origin master ``` (ssh bağlantısında bunu bir kez yazdıktan sonra sadece git push kullanarak aynı branch(master/main) üzerinde push işlemi gerçekleştirilebilir. )

---

### 2. Branch (Dallanma) <a name="branch"></a>

Github’ın en güzel özelliklerinden bir tanesi branch sistemidir. Üzerinde çalıştığınız bir projede önemli bir değişiklik yapmak istiyorsunuz ve bu değişiklik zaman alacak hatta birçok kodu etkileyecek, ekip arkadaşlarınızın bu süreçten etkilenmemesi için sadece kendinizin ya da küçük bir ekibin çalışacağı bir ortam yaratmak istiyorsunuz… 

İşte burada orjinal projenin bir kopyasını alarak farklı bir branch açıyorsunuz, burada istediğiniz kadar değişiklik yapın, push’layın, commit dizileri oluşturun vb., bunlar sadece bu branch üzerinde olacaktır. En sonunda istediğiniz değişiklik tamamlandığında main branch ile bu branch'in merge(birleştirme) işlemi gerçekleştirilebilir.

___NOT:___ bu komutlar lokal üzerinde tanımlanan branch’ler üzerinde kullanılmalıdır. Remote branch işlemleri için daha fazla detay -> [Remote Operations - Branches](https://www.atlassian.com/git/tutorials/using-branches)

Var olan branch’leri kontrol edin

> ``` git branch ```

Yeni bir branch oluşturun

> ``` git branch branch_name ```

Bulunduğunuz branch’i değiştirin 

> ``` git checkout branch_name ```

Branch silin

> ``` git branch -d branch_name ```

Değişiklikleri remote branch’e push

> ``` git push origin branch_name ```

İki branch’i birleştirme

> ``` git merge (source branch) (target branch) ```

---

### 3. Git İşlem Geri Alma ( Undoing In Git) <a name="undoing"></a>

Eğer git add ile değişiklikleri lokal reponuza kaydetmişseniz bu işemleri geri almak için 

> ``` git reset ```

Belirli değişklikleri geri almak için 

> ``` git reset FILE_NAME ```

Son commit’i geri alma

> ``` git reset HEAD~ ```

> ```git log ``` ile yapılan commit’ler listelenebilir ve commit numaraları kullanılarak özel bir commit üzerinden de işlemler yapılabilir.

git diff kullanarak branch’ler arasındaki farkliılıklar bulunabilir

> ```git diff (other_branch’s_name)``` or ``` git diff —stat (other_branch’s name) ```

Genel bir değişiklik istatistiği 

> ``` git log —stat ```


___Remote repodaki güncellemeleri lokala almak___

Ekip çalışmalarında projenin güncel halinin lokal’de de bulunması gerektiğinden dolayı pull işlemi ile lokaldkei repomuzu güncel tutmalıyız.

> ``` git pull ```

Benzer bir işlem olan git fetch ve git pull arasındaki farklara dair çok güzel bir açıklama -> [Pull & Fetch](https://stackoverflow.com/questions/292357/what-is-the-difference-between-git-pull-and-git-fetch)

---

### 4. PULL REQUEST <a name="pr"></a>

Open source’u open source yapan özellik, yazılım dünyasında kısaca PR yani Pull Request

İstediğiniz herhangi bir public projeyi github'da kendi repolarınız arasına alabilir(fork) ve istediğiniz gibi değişiklikler yapabilirsiniz. Hatta bu değişiklikleri fork ettiğimiz reponun sahibine bile gönderebiliriz - > PR. 

Eğer yaptığımız değişiklikler projeyi geliştiriyor, bug gideriyor veya herhangi bir katkıda bulunuyorsa proje sahibi sizin yaptığınız bu değişiklikleri orjinal repoya dahil edebilir. İşte bu işlem Pull Request sayesinde gerçekleştirilebilmektedir.

Adım Adım PR:

1.  PR yapmak istediğniz Repoyu bulun ve repo ana sayfasına gidin
2.  Sağ üstteki FORK butonuna tıklayın ve repoyu kendi repolarınıza kopyalayın.
3.  Kendi repolarınıza gidin ve bu fork edilmiş reponuza tıklayın
4.  Code kısmından repo linkini alın ve git clone (bir önceki başlıklarda anlatılan) ile lokal klasörünüze klonlayın
5.  İstediğiniz değişiklikleri yapın ve add commit push işlemlerini tamamlayın
6.  Github’a gidin ve projenizin son hali için ___Compare and Pull Request Butonuna__ Tıklayın

Burada ___önemli___ olan detaylar, commit başlıkları olabildiğince kısa ve öz olmalı 

- Add, Update, Fix gibi aksiyon belirten kelimeler kullanılmalı
- Noktalamalardan kaçının
- Takım içerisinde kullanılan dile bağlı kalın

PR açıklamalarında uzun uzun paragraflar değil, listelenmiş halde yapılan değişiklikler commit başlığına göre biraz daha detaylandırılmış hali ile basit bir şekilde açıklanabilir.

---
---

__SON__

Bu komutlar ile neredeyse tüm git-github işlemleri gerçekleştirilebilir. Pratik yaparak komut satırı/terminal üzerinde kısa sürede hız kazanılabilir.

Ayrıca clone, branch, merge, PR gibi temel kavramların görselleştirilmiş halleri veya animasyon videoları ile pekiştirilmesi git öğrenme sürecini hem daha anlaşılır yapacak hem de daha eğlenceli hale getirecektir. Git ve Github yazılım dünyasının vazgeçilmezidir. Open-Source’u destekleyelim.

__ENES ÇAVUŞ__  - Notes about Most Used Git Commands - Last Update August 2021