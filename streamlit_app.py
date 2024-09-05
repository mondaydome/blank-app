import streamlit as st

abstand_1: str = "\n\n"

image_1: str = "https://cdn.discordapp.com/attachments/1125323944476549171/1279034021057396746/mondaydome_two_people_standing_apart_looking_at_each_other_frie_dea8f1e3-853c-432a-aff9-7bfdd1b073a3.png?ex=66d99041&is=66d83ec1&hm=b36c9a1e7ec8a5c153db54733d7ca1f5bcef3e0aafa2a8d7e978f2398fd69d46&"
image_1_caption: str = 'Symbolbild - Quelle: Midjourney'

image_2: str = "https://cdn.discordapp.com/attachments/1125323944476549171/1279033253109567579/mondaydome_two_people_standing_in_distance_looking_at_each_othe_7ce9d997-dd10-4cc2-8436-2f86db2a6f94.png?ex=66da384a&is=66d8e6ca&hm=fde86054e2c660fc5a97df792b928f192f673a8e6cb7909d6fee1b0c1eca0653&"
image_2_caption: str = "Symbolbild - Quelle: Midjourney"

image_3: str = "https://cdn.discordapp.com/attachments/1125323944476549171/1279033291625992252/mondaydome_two_people_standing_looking_at_each_other_friendly_f_24170d83-29f3-4f07-8cd1-ae3322e82d36.png?ex=66da3854&is=66d8e6d4&hm=87d3ee2b7373d71f9d1da7e5ec0d84f523ba2b9f2dd542dffa864be356d2e874&"
image_3_caption: str = "Symbolbild - Quelle: Midjourney"

image_4: str = "https://cdn.discordapp.com/attachments/1125323944476549171/1279033599688970354/mondaydome_two_people_standing_apart_looking_at_each_other_frie_88c79741-5524-4013-923a-ae8c21479840.png?ex=66da389d&is=66d8e71d&hm=344d683a423bac4e4640c8a451acb469b6de7874cfbd8b9106d9459189006385&"
image_4_caption: str = "Symbolbild - Quelle: Midjourney"

title: str = "Gut getrennt :memo::white_check_mark::relieved:"
header: str = "Unser Projekt hilft Familien, den schwierigen Trennungsprozess durch eine faire und verständliche Unterhaltsberechnung emotional zu entlasten. Mit unserer Software und KI erstellen wir Trennungsvereinbarungen und Unterhaltsberechnungen, um eine einvernehmliche Trennung ohne hohe Anwaltskosten zu ermöglichen. Unterstützen Sie uns dabei, einen Prototyp zu entwickeln und unserer Vision einer ’guten Trennung’ für alle Beteiligten einen Schritt näher zu kommen."
sub_title_1: str = "Unterstütze uns jetzt auf wemakeit.com!"

sub_title_trennungsgeschichte: str = "Meine Trennung"
text_trennungsgeschichte: str = "Im Herbst 2020 entschieden meine Ex-Partnerin und ich uns zur Trennung. Wir wandten uns an den Sozialdienst für eine Trennungsvereinbarung, stiessen jedoch bei der Barunterhaltsberechnung auf unverständliche Erklärungen. \nMeine Ex-Partnerin beauftragte einen Anwalt, woraufhin ich ebenfalls einen nahm. Nach Anpassungen der Vereinbarung durch beide Seiten reichten wir sie bei der KESB ein, die sie wegen Einseitigkeit ablehnte. \nDie Berechnung und Vereinbarung mussten erneut überarbeitet werden, doch es blieb der Eindruck, dass selbst die Anwälte die Berechnungen nicht völlig verstanden. Das Problem lag in der verwendeten Technologie – einem unübersichtlichen Excel-Dokument. Als Leiter innovativer Softwareprojekten bin ich überzeugt, moderne Software mit klaren Visualisierungen könnte hier Abhilfe schaffen."

sub_title_vision: str = "Unsere Vision"
text_vision: str = "Eine intuitive Webapplikation, die den Trennungsprozess vereinfacht – auch mobil. Mit benutzerfreundlichen Eingabemasken und klaren Erklärungen zur Barunterhaltsberechnung, unterstützt durch verständliche Visualisierungen. Ein KI-gestützter Trennungsvereinbarungs-Generator hilft, ohne juristische Vorkenntnisse, eine faire Vereinbarung zu erstellen. Ziel: Emotionen aus der Diskussion nehmen und den Trennungsprozess sachlich und fair gestalten, für ein gutes Miteinander nach der Trennung."

sub_title_crowdfunding: str = "CrowdFunding"
text_crowdfunding: str = "Unser Ziel ist es, mit eurer Unterstützung die Entwicklung eines ersten Prototyps unserer Webapplikation zu finanzieren. Dieser Prototyp soll beweisen, dass ein grosses Bedürfnis nach einer einfachen, transparenten Lösung für die Berechnung des Barunterhalts besteht. Mit dem Prototypen möchten wir ausserdem die Aufmerksamkeit von Behörden gewinnen und deren Unterstützung für das Projekt sichern. Gemeinsam machen wir so den ersten Schritt hin zu unserer Vision: Eine faire und verständliche Lösung, die emotionale Konflikte bei Trennungen reduziert und den Prozess für alle Beteiligten erleichtert."

sub_title_dank: str = "Vielen Dank für deine Unterstützung!"
text_dank: str = "Vielen Dank für deine Unterstützung. Du hilfst mir hier bei meinem Herzensprojekt: Ich will faire und verständliche Trennungsvereinbarungen für euch, für ein gutes Miteinander nach der Trennung! "

text_impressum: str = "Dominic Michel, Bremgarten b. Bern"
link_linkedin: str = "https://www.linkedin.com/in/dominic-michel-digitaltransformierer/"
link_label_linkedin: str = text_impressum

button_1_text: str = "Go to wemakeit.com"
button_1_URL: str = "https://wemakeit.com/projects/gut-getrennt?locale=de#rewards"

st.image(image_1)
st.caption(image_1_caption)

st.title(title)
st.write(header)
st.write(abstand_1)

st.subheader(sub_title_1) 
st.link_button(button_1_text, button_1_URL)
st.write(abstand_1)


st.subheader(sub_title_trennungsgeschichte)
st.write(text_trennungsgeschichte)
st.write(abstand_1)
st.image(image_2)
st.caption(image_2_caption)

st.subheader(sub_title_vision)
st.write(text_vision)
st.write(abstand_1)
st.image(image_3)
st.caption(image_3_caption)

st.subheader(sub_title_crowdfunding)
st.write(text_crowdfunding)
st.write(abstand_1)
st.image(image_4)
st.caption(image_4_caption)


st.subheader(sub_title_1) 
st.link_button(button_1_text, button_1_URL)

st.subheader(sub_title_dank)
st.write(text_dank)
st.page_link(link_linkedin, label=link_label_linkedin)
st.write(abstand_1)