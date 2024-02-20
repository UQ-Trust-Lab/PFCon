from selenium.common.exceptions import NoSuchElementException   
from selenium.common.exceptions import WebDriverException



services_name_list_2 = ["ios_calendar","dart","dribbble_job_board","android_device","ballotpedia","app_store","do_button","grants","epa","ios_health","airnow","bea","ifttt","electricitymap","usda","cdc","pew_research","uscert","indeed","android_messages","android_photos","reddit","usagov","wwf","fcu_tod","hacker_news","sensate","propublica","smarthon","sfgate","do_note","eff","seeburg","humanunited","aclu","caltrain","epicjobs","optus_smart_living","songkick","space","us_independence_day","brainstorm9","npr","intuiface","era","pg_e","ios_reading_list","clinicaltrials","android_wear","dod","sfmta","slickdeals","elektrum","sunrise_sunset_org","bond","unodc","we_work_remotely","flickr","finance","pinboard","pocket","longreads","evernote","loc","instagram","facebook_pages","twitter","wordpress","foursquare","voip_calls","giphy","king_county_metro","email_digest","gmail","nsf","fcc","dol","naacp","nvd","date_and_time","android_phone","diigo","wolfram_data_drop","soundcloud","cta","buffer","fleep","oge","blogger","green_light_signal","feed","bitly","careers_org","brainyquote","dos","box","tampa","bart_delay","apa","slashdot","itchio","weather","yelp","sms","if_notifications","nano_lol","isitchristmas","blink1","email","android_battery","who","muslim_prayer_time","nj_transit","foxnews","ios_photos","ios_contacts","imf","ios_reminders","sec","smartthings","do_camera","vf_maskreminder","nytimes","phone_call","eia","iot_podcast","smartlouisville","texas_legislature","IQAir","delicious"]
#services_name_list_1 = ["dothub","bdrthermeagroup","maker_webhooks","blueconnect","bang_olufsens_beo_link_gateway","netatmo_security","m2m_services","scoutalarm","akari_ai","whisker","nomos_system","aura_air","lexi","Pixoo_64","haven_iaq","convo","hc_cleaning_robot","domovea","musixmatch","grouplotse","somfy_tahoma_north_america","strava","ezviz","wemo_slowcooker","aimore","nikohomecontrol","wink_shortcuts","lightwaverf_events","spotcam","wemo_coffeemaker","intesishome","wiser_air","lightform_cloud","DawnHouse","augusthome","alexa_doorbell","onenote","verizon_cloud","i_zone","switchbot","link_smart_home","hc_coffee_machine","asana","vont_home","view_prod","eight","tumblr","SamsungRobotVacuum","smartliving_osum","caleo","podio","littlebits","todoist","hubitat","irobot","ubibot","uplinkremote","apilio","putio","hager_iot","wemo_airpurifier","amazon_alexa","skyroam","digitalstrom","u_tec_ultraloq","aypro","notifymyecho","ge_appliances_washer","blink_eu","microsoft_todo","wemo_light_switch","monzo","nVent_Nuheat","livesmart","telegram","magichue","awair","homelyenergy","hc_cook_processor","somfy_connexoon_asia_oceania","ihomecontrol","roomme","airtouch","narro","trello","disec_tronic","tochie_speaker","smanos","atmoph","lightwaverf_heating","ComEd","somfy_thermostat","tado_heating","dooya_connector","daskeyboardq","product_hunt","attm2x","medium","XHouseIOT","fl_1000_leak_detector","rain_machine","porkfolio","dominos","qnap","LDS_AiDot","automateshades","bocco","sesame","fansync","ecobee","zohocliq_in","tecla","zoom_phone","genius_hub","lovebox","futurehome","myfox_homecontrol","pagerduty","invoxia_tracker","coinbase","ge_appliances_cooking","Mapei_Mapeheat","indegoconnect","hc_fridge","slack","abode","cielo_home","vestaboard","openhab","roostermoney","beeminder","google_calendar","chacon_dio","agile_octopus","fing","turntouch","ergosmartbed","SAFEBYHUB6","dobiss","sonos","google_drive","nuki_opener","easyftp","ring","bosma","vesyncSwitchOnline","ge_appliances_dishwasher","weatherflow","vimeo","easycontrol_bosch","mailchimp","LinkMyPet","powahome","sRemo","homeseer","watts","muilab","airpatrol","isecurityplus","ambiclimate","lutron_caseta_wireless","ohmconnect","adafruit","google_wifi","somfy_connexoon","AlexaActionsByMkzense","garadget","nimbus_note","microsoft_teams","nuki","ti_do","mydlink","somfy_tahoma_bee","airtable","Ratoc_remocon","zohocliq","gideon","honeywell_lyric","lametric","stockimo","MSmartA1","groupme","bluelink","datadotworld","mymilan","hive_active_plug","trane_home","SamsungWasher","honeywell_total_connect_comfort","trakt","aquanta","bbox_miami","hue","harvest","filtrete","boundary","electrolux","lennoxicomfort","instapaper","patreon","wemo_humidifier","arlo","sateraito_office","usign","watttime","logitech_pop","telldus","AerialTechnologies","intelligent_voice","ambient_weather","hopscotch","google_tasks","feedly","Smitch","aros","asusrouter","automateshades_v2","simcam","metronet","webehome","hive_active_light","Confio","withings","myuplink","musaic","myq_devices","onedrive","noonhome","MyCurtains","line","resideo_total_connect","active_sleep","blickdomi_compact","nest_cam","ihaus_smoke_detector","orion","sensibo","tesco","chatwork","zohocliq_au","PIXIEPLUS","tailwind","bitmark","brilliant_nexus","SamsungRefrigerator","discord","harmony","WithingsSleep","eggminder","true_energy_norway","oticon","garagewifi","tado_hot_water","zuluhood","meistertask","foobot","finder_yesly","iotics","rescuetime","SAUTER_Cozytouch","weebly","sense_energy_monitor","gardena_smart_system","skylinknet","honeywell_evohome","histre","chiekoo_bell","lightwaverf_lighting","heatzy","go","alpaca","tracmo","misfit","clicksend","auroome","mystrom","hc_hob","camio","shopyourway","neato","my_leviton","flapz_board","tplink_router","zeeq","brilliant_smart","virtualbuttons","ewelink","spontit","moodo","savetheproof","vesync","fulltime_fullarm","day_one","weara","emfit","xtactor","particle","streamr_network","heatmiser","reposit","ge_appliances_geospring","epion","rust","viva","vybit","ge_appliances_dryer","netatmo_thermostat","gogogate","google_contacts","meross","smarter","MSmartAC","wirelesstag","dormakabaTAS","WattuneedBatteryUP","LinkJapan_eHome","followupcc","blink","swannsecurity","qapital","NethomePlusA1","invoxia_triby","fletti","dozens","Air_Monitor","docsend","nest_protect","samsungairconditioner","coqon","swidget","github","kasa","pushcut","rachio_iro","spotter","oco_camera","moretrees","vesyncIftttAirPurifier","teletrac","linkedin","hive_active_heating","timelines","easycsv","smart_home_solution","automower","gira","zynect_sensors","kumocloud","cloudrain","Huma_i","bloomsky","energeasyconnect","american_standard_home","automator","alko_smart_garden","bernafon","pavlok","vesyncBulb","kronaby","fibaro","sowee","wemo_maker","iottysmarthome","aura","selock","skybell","hc_wine_cooler","tado_air_conditioning","nibe_uplink","samsungairpurifier","otiom","hive_view","bluebyadt","vesyncDimmer","Philips_air_purifer","airthings","youtube","livy_protect","ORBneXt","updraft","ispy_agent","osumsmart","energenie_mi_home","go_raylogic","clova","knocki","smartap_shower","Aqara_Home_EU","timetogowild","facebook","aisync","somfy_mylink","LinkShades","blurams","miyo","routee","slbus","sonic","honeywell_round","livisi","notion_so","hc_hood","ivideon","BG_HOME","safetrek","hc_washer","thinga","homey","relay","ATLANTIC_Cozytouch","thinka","dropbox","wattio_smarthome","yolink","nexx","ge_appliances_refrigerator","callmebot","zense_home","angelcam","nature","kubu_smart_lock","firedesk","sharpr","instar","uhoo","nefit_easy","True_Energy","envoy","remoplus","konkasmart","EDFPlages","wiser_heat","asuszeneye","tis_smart_home","spotify","wyzecam","aico","tecan_connect","amazonclouddrive","AnywareServices","jaguar_watches","ooma","nimbus","ihome_enhance","habitify","nemy","trigger_cmd","welltory","soma","festina_watches","fitbit","toodledo","twitch","SamsungRoomAirconditioner","nice","newsblur","smappee","notebook","everykit","jotform","lotus_watches","notion","Optoma","amplenote","Amba","donation_manager","wemo_insight_switch","broadlink","cisco_spark","works_with_cavius","pivot_power_genius","wemo_lighting","somfy_protect","bouncie","boxcar_2","netatmo","google_assistant","mobilinc","smartnest","glanceclock","mysa_thermostat","hc_oven","phyn","surveymonkey","pryv","woopla","hc_dishwasher","kaiterra","asukaiot","NethomePlusAC","aquarea_smart_cloud","lifx","wemo_dimmer","hc_dryer","orro","MsmartMicrowave","google_docs","delphy","tmt_chow","dlink_wifi_router","imwork","zware","smartliving","wifiplug","nanoleaf","salesforce","hive_view_outdoor","hearlink","simplehuman","moonside","wemo_switch","neosmartblinds","AduroSmart","inoreader","zohocliq_eu","switchur","narrative","sighthound","cloud_bot","withingshome","thermosmart","wemo_motion","zubie","powerview","pebblebee","beam","yeelight","google_sheets","pushover","freedompro","typeform","nest_thermostat","cityofbeverlyhills","linkdesk","bocco_emo","warmup_smart_thermostat","voicemonkey","omninewlab","coresmarthome","logitech_circle","wemo_outdoor_plug","hella_onyx","ialarmxr","wiz","lightwaverf_power","oval_smart_home","dondeesta","gewiss_home","graspio","leeo","Aqara_Home","econnect","idevices","seitronsmart","unforgettable_me","square","sengled","air_q","garageio","zoom","fujitsu_general_limited","qualitytime","THERMOR_Cozytouch","govee","pushsafer","tantiv4","planex","slide_by_iim","dailymotion","fiverr","somfy_tahoma","zohocliq_cn","daikin_online_controller","location","raindrop","smartlife","pushbullet","rememberthemilk","danalock","netro","flic","beseye","Lytmi","MagicLight","nexia","remotelync","maestro_by_stelpro","publer","caavo","ge_appliances_wac","TickTick","yardian","mesh","home_navigation"]
baned_services_name = [
    #need manuliy auth
    "adafruit",
    #cannot be login in, need physical devices
    "agile_octopus",  "aisync", "IQAir", "air_q", "abode", "Air_Monitor", "active_sleep", "AduroSmart", "airthings",
    "airtouch", "akari_ai", "Amba", "ambiclimate", 
    "aico", "LDS_AiDot", "airpatrol", "Aqara_Home_EU", "Aqara_Home", 
    "aquarea_smart_cloud", 
    # no connection for such service
    "airnow",  "apa",
    # require android/ ios app to auth permission:
    "android_battery", "android_device", "android_phone", "android_photos", "android_messages",
    ]


auth_successfully = [
    "moretrees", "intesishome", "airtable", "alko_smart_garden", "AlexaActionsByMkzense",
    "voicemonkey", "alpaca", "amazon_alexa", "amazonclouddrive", "ambient_weather",
    "AerialTechnologies", "aimore", "alexa_doorbell", "american_standard_home", 
    "amplenote", "angelcam", "apilio", "AnywareServices",
    "aquanta", "arlo",
]

def possible_xpath(kw):
    xpath_list = []
    xpath_list.append("//button[@type='" + kw + "']")
    xpath_list.append("//button[@value='" + kw + "']")
    xpath_list.append("//button[contains(text(),'" + kw + "')]")
    xpath_list.append("//input[@placeholder='" + kw + "']")
    xpath_list.append("//input[@type='" + kw + "']")
    return xpath_list

def check_exists_by_path(webdriver,xpath):
    try:
        webdriver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_id(webdriver, id):
    try:
        webdriver.find_element_by_id(id)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_name(webdriver, name):
    try:
        webdriver.find_element_by_name(name)
    except NoSuchElementException:
        return False
    return True
    
def check_exists_by_css_selector(webdriver, css_selector):
    try:
        webdriver.find_element_by_css_selector(css_selector)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_class_name(webdriver, class_name):
    try:
        webdriver.find_element_by_class_name(class_name)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_link_text(webdriver, text):
    try:
        webdriver.find_element_by_link_text(text)
    except NoSuchElementException:
        return False
    return True

def check_vaild_connection_url(url):
    tokens = url.split("/")
    if len(tokens) < 2:
        return False
    name = tokens[len(tokens) - 2]
    print("service name: " + name)
    if name in auth_successfully:
        #print("already fetched auth info")
        return False
    if name in baned_services_name:
        #print("already banned auth")
        return False
    if name in services_name_list_2 and name not in baned_services_name and name not in auth_successfully:
        return True
    return False

def check_browser_url(webdriver,url):
    try:
        webdriver.get(url)
    except WebDriverException:
        print("unable to connect to given url")
        return False
    return True
        
def get_visible_text_from_page(webdriver):
    try:
        webdriver.find_element_by_tag_name('body')
    except NoSuchElementException:
        return ""
    
    page_text = webdriver.find_element_by_tag_name('body').text
    return page_text

# passwd1
pwd_1 = ["netatmo", "flapz", "oge", "agile_octopus"]

# passwd2
pwd_2 = ["link_smart_home", "lutron", "asuszeneye", "ge_appliances", "nemy", "woopla", "zware"]

# passwd3
pwd_3 = ["musixmatch", "samsung", "Samsung", "aquarea", "smartlife"]


# passwd4
pwd_5 = [
    "arlo", "bluebyadt", "hc_", "/line/", "lametric", "smartlife", "myfox",
    "kumocloud", "mystrom", "vesync", "blink", "chacon_dio", "brilliant", "beseye", "bosma",
    "eight", "ezviz", "line", "ecobee", "fansync",
]

def get_special_pwd(url):
    for kw in pwd_1:
        if kw in url:
            return "***"

    for kw in pwd_2:
        if kw in url:
            return "***"

    for kw in pwd_3:
        if kw in url:
            return "***"
     
    for kw in pwd_5:
        if kw in url:
            return "***"
    
    return "***"