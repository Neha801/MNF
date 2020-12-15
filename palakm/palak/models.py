from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.postgres.fields import JSONField,ArrayField


genre_choice = ( 
    ("Action", "Action"), 
    ("Adventure", "Adventure"), 
    ("Animation", "Animation"), 
    ("Biography", "Biography"), 
    ("Drama", "Drama"), 
    ("Comedy", "Comedy"), 
    ("War", "War"), 
    ("Thriller", "Thriller"), 
)
language_of_action_line_choice =(
    ("Hindi","Hindi"),
    ("English","English"),
    ("German","German"),
)
language_of_dialogues_choice =(
    ("Hindi","Hindi"),
    ("English","English"),
    ("German","German"),
)
script_written_in_choice =(
    ("Roman","Roman"),
    ("Devnagri","Devnagri"),
)
time_choice =(
    ("Modern","Modern"),
    ("Contemporary","Contemporary"),
    ("Ancient","Ancient"),
)
country_choice =(
    ("Afghanistan","Afghanistan"),
    ("Åland Islands","Åland Islands"),
    ("Albania","Albania"),
    ("Algeria","Algeria"),
    ("American Samoa","American Samoa"),
    ("Andorra","Andorra"),
    ("Angola","Angola"),
    ("Anguilla","Anguilla"),
    ("Antarctica","Antarctica"),
    ("Antigua and Barbuda","Antigua and Barbuda"),
    ("Argentina","Argentina"),
    ("Armenia","Armenia"),
    ("Aruba","Aruba"),
    ("Australia","Australia"),
    ("Austria","Austria"),
    ("Azerbaijan","Azerbaijan"),
    ("Bahamas","Bahamas"),
    ("Bahrain","Bahrain"),
    ("Bangladesh","Bangladesh"),
    ("Barbados","Barbados"),
    ("Belarus","Belarus"),
    ("Belgium","Belgium"),
    ("Belize","Belize"),
    ("Benin","Benin"),
    ("Bermuda","Bermuda"),
    ("Bhutan","Bhutan"),
    ("Bolivia, Plurinational State of","Bolivia, Plurinational State of"),
    ("Bonaire, Sint Eustatius and Saba","Bonaire, Sint Eustatius and Saba"),
    ("Bosnia and Herzegovina","Bosnia and Herzegovina"),
    ("Botswana","Botswana"),
    ("Brazil","Brazil"),
    ("British Indian Ocean Territory","British Indian Ocean Territory"),
    ("Brunei Darussalam","Brunei Darussalam"),
    ("Bulgaria","Bulgaria"),
    ("Burkina Faso","Burkina Faso"),
    ("Burundi","Burundi"),
    ("Cambodia","Cambodia"),
    ("Cameroon","Cameroon"),
    ("Canada","Canada"),
    ("Cape Verde","Cape Verde"),
    ("Cayman Islands","Cayman Islands"),
    ("Central African Republic","Central African Republic"),
    ("Chad","Chad"),
    ("Chile","Chile"),
    ("China","China"),
    ("Christmas Island","Christmas Island"),
    ("Cocos (Keeling) Islands","Cocos (Keeling) Islands"),
    ("Colombia","Colombia"),
    ("Comoros","Comoros"),
    ("Congo","Congo"),
    ("Congo, the Democratic Republic of the","Congo, the Democratic Republic of the"),
    ("Cook Islands","Cook Islands"),
    ("Costa Rica","Costa Rica"),
    ("Côte d'Ivoire","Côte d'Ivoire"),
    ("Croatia","Croatia"),
    ("Cuba","Cuba"),
    ("Curaçao","Curaçao"),
    ("Cyprus","Cyprus"),
    ("Czech Republic","Czech Republic"),
    ("Denmark","Denmark"),
    ("Djibouti","Djibouti"),
    ("Dominica","Dominica"),
    ("Dominican Republic","Dominican Republic"),
    ("Ecuador","Ecuador"),
    ("Egypt","Egypt"),
    ("El Salvador","El Salvador"),
    ("Equatorial Guinea","Equatorial Guinea"),
    ("Eritrea","Eritrea"),
    ("Estonia","Estonia"),
    ("Ethiopia","Ethiopia"),
    ("Falkland Islands (Malvinas)","Falkland Islands (Malvinas)"),
    ("Fiji","Fiji"),
    ("Finland","Finland"),
    ("France","France"),
    ("French Guiana","French Guiana"),
    ("French Polynesia","French Polynesia"),
    ("French Southern Territories","French Southern Territories"),
    ("Gabon","Gabon"),
    ("Gambia","Gambia"),
    ("Georgia","Georgia"),
    ("Germany","Germany"),
    ("Ghana","Ghana"),
    ("Gibraltar","Gibraltar"),
    ("Greece","Greece"),
    ("Greenland","Greenland"),
    ("Grenada","Grenada"),
    ("Guadeloupe","Guadeloupe"),
    ("Guam","Guam"),
    ("Guatemala","Guatemala"),
    ("Guernsey","Guernsey"),
    ("Guinea","Guinea"),
    ("Guinea-Bissau","Guinea-Bissau"),
    ("Guyana","Guyana"),
    ("Haiti","Haiti"),
    ("Heard Island and McDonald Islands","Heard Island and McDonald Islands"),
    ("Holy See (Vatican City State)","Holy See (Vatican City State)"),
    ("Honduras","Honduras"),
    ("Hong Kong","Hong Kong"),
    ("Hungary","Hungary"),
    ("Iceland","Iceland"),
    ("India","India"),
    ("Indonesia","Indonesia"),
    ("Iran, Islamic Republic of","Iran, Islamic Republic of"),
    ("Iraq","Iraq"),
    ("Ireland","Ireland"),
    ("Isle of Man","Isle of Man"),
    ("Israel","Israel"),
    ("Italy","Italy"),
    ("Jamaica","Jamaica"),
    ("Japan","Japan"),
    ("Jersey","Jersey"),
    ("Jordan","Jordan"),
    ("Kazakhstan","Kazakhstan"),
    ("Kenya","Kenya"),
    ("Kiribati","Kiribati"),
    ("Korea, Democratic People's Republic of","Korea, Democratic People's Republic of"),
    ("Korea, Republic of","Korea, Republic of"),
    ("Kuwait","Kuwait"),
    ("Kyrgyzstan","Kyrgyzstan"),
    ("Lao People's Democratic Republic","Lao People's Democratic Republic"),
    ("Latvia","Latvia"),
    ("Lebanon","Lebanon"),
    ("Lesotho","Lesotho"),
    ("Liberia","Liberia"),
)
city_choice =(
    ("Delhi","Delhi"),
    ("Chennai","Chennai"),
    ("Mumbai","Mumbai"),
)
gender_choice =(
    ("Male","Male"),
    ("Female","Female"),
)
age_group_choice =(
    ("Child","Child"),
    ("Infant","Infant"),
    ("Young","Young"),
    ("Adult","Adult"),
    ("Senior Age","Senior Age"),
)
music_choice =(
    ("MNF Men Voice 1","MNF Men Voice 1"),
    ("MNF Women Voice 1","MNF Women Voice 1"),
    ("MNF child Voice 1","MNF child Voice 1"),
    ("MNF Adult Voice 1","MNF Adult Voice 1"),
       
)
class Script_info(models.Model):
    msg_id = models.AutoField(primary_key = True)
    script_title = models.CharField(max_length=50)
    Author_name = models.CharField(max_length=50)

    genre= MultiSelectField(choices = genre_choice, default = '')

    language_of_action_line= models.CharField(max_length=50, choices = language_of_action_line_choice, default = '')

    language_of_dialogues = models.CharField(max_length=50,choices = language_of_dialogues_choice, default = '')

    script_written_in = models.CharField(max_length=50,choices = script_written_in_choice, default = '')

    time =models.CharField(max_length=50,choices = time_choice, default = '')

    country = models.CharField(max_length=50,choices = country_choice, default = '')
    city =models.CharField(max_length=50,choices = city_choice, default = '')
    scriptfile = models.FileField(upload_to = 'scriptfile',default = '')
    
    def __str__(self):
        return self.script_title

class Character_edit(models.Model):
    msg_id = models.AutoField(primary_key = True)
    character_image = models.ImageField(upload_to = 'character_image',default = '')
    character_name = models.CharField(max_length=50,default = '')
    gender= MultiSelectField(choices = gender_choice, default = '')
    age_group = models.CharField(max_length=50,choices = age_group_choice, default = '')
    music = models.CharField(max_length=50,choices = music_choice, default = '')
    
    def __str__(self):
        return self.character_name

class Budget(models.Model):
    
    Actors=models.FloatField(null=True, blank=True, default=0.0)
    Other_Actors=models.FloatField(null=True, blank=True, default=0.0)
    Production=models.FloatField(null=True, blank=True, default=0.0)
    Director=models.FloatField(null=True, blank=True, default=0.0)
    Producer=models.FloatField(null=True, blank=True, default=0.0)
    post_production=models.FloatField(null=True, blank=True, default=0.0)
    Legal=models.FloatField(null=True, blank=True, default=0.0)
    Marketing=models.FloatField(null=True, blank=True, default=0.0)
    Miscellaneous=models.FloatField(null=True, blank=True, default=0.0)
    Total_Budget=models.FloatField(null=True, blank=True, default=0.0)
      
class Stage2(models.Model):
      id=models.CharField(max_length=100,primary_key=True)
      Script=models.CharField(max_length=50, blank=True)
      video_time_produced=models.FloatField()
      total_shoot_days=models.IntegerField()
      all_locations=ArrayField(models.CharField(max_length=50), blank=True,null=True)
      character_importance=JSONField()
      all_actors=ArrayField(models.CharField(max_length=50), blank=True ,null=True)
      total_scenes=models.IntegerField()
      extras=ArrayField(models.CharField(max_length=50,blank=True,null=True))
      stunts=models.BooleanField()
      vehicles=ArrayField(models.CharField(max_length=50), blank=True,null=True)
      props=ArrayField(models.CharField(max_length=50,blank=True,null=True))
      special_effect=models.BooleanField()
      costumes=ArrayField(models.CharField(max_length=50), blank=True,null=True)
      makeup=ArrayField(models.CharField(max_length=50), blank=True,null=True)
      sound=ArrayField(models.CharField(max_length=50), blank=True,null=True)
      set_dressing=ArrayField(models.CharField(max_length=50,blank=True,null=True))
      greenery=ArrayField(models.CharField(max_length=50,blank=True,null=True))
      livestock=ArrayField(models.CharField(max_length=50), blank=True,null=True)
      animal_handler=models.BooleanField()
      music=ArrayField(models.CharField(max_length=50,blank=True,null=True))
      special_equipment=ArrayField(models.CharField(max_length=50,blank=True,null=True))
      security=models.BooleanField()
      additional_labor=ArrayField(models.CharField(max_length=50,blank=True,null=True))
      optical_fx=models.IntegerField()
      mechanical_fx=models.IntegerField()
      miscellaneous=ArrayField(models.CharField(max_length=50,blank=True,null=True))

      def __str__(self):
            return self.Script
      

