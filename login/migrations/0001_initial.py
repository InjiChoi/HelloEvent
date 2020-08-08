# Generated by Django 3.0.9 on 2020-08-07 20:23

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator_name', models.CharField(max_length=100, verbose_name='크리에이터명')),
                ('creator_photo', models.ImageField(upload_to='creator_photo/%Y/%m/%d/')),
                ('desc', models.TextField(blank=True)),
                ('cr_area', models.CharField(choices=[('Seoul', '서울'), ('Incheon', '인천'), ('Gyeonggi', '경기'), ('Gangwon', '강원'), ('Daejeon', '대전'), ('Daegu', '대구'), ('Ulsan', '울산'), ('Busan', '부산'), ('Gwangju', '광주'), ('Chungcheong', '충청'), ('Jeolla', '전라'), ('Gyeongsang', '경상'), ('Jeju', '제주')], max_length=100, verbose_name='지역')),
                ('cr_seoul_city', models.CharField(choices=[('Gangnam', '강남구'), ('Songpa', '송파구'), ('Seocho', '서초구'), ('Gangdong', '강동구'), ('Gwanak', '관악구'), ('Yeongdeung', '영등포구'), ('Gangseo', '강서구'), ('Yangcheon', '양천구'), ('Guro', '구로구'), ('Geumcheon', '금천구'), ('Jongno', '종로구'), ('Jung', '중구'), ('Dongdaemun', '동대문구'), ('Jungrang', '중랑구'), ('Mapo', '마포구'), ('Yongsan', '용산구'), ('Seongdong', '성동구'), ('Gwangjin', '광진구'), ('Eunpyeong', '은평구'), ('Seodaemun', '서대문구'), ('Seongbuk', '성북구'), ('Gangbuk', '강북구'), ('Dobong', '도봉구'), ('Nowon', '노원구')], max_length=100)),
                ('cr_theme', models.CharField(choices=[('BUSKING', '버스킹'), ('FLEE', '플리마켓'), ('EXHIBITION', '전시회')], max_length=100, verbose_name='테마')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nickname', models.CharField(max_length=100, verbose_name='닉네임')),
                ('area', models.CharField(choices=[('Seoul', '서울'), ('Incheon', '인천'), ('Gyeonggi', '경기'), ('Gangwon', '강원'), ('Daejeon', '대전'), ('Daegu', '대구'), ('Ulsan', '울산'), ('Busan', '부산'), ('Gwangju', '광주'), ('Chungcheong', '충청'), ('Jeolla', '전라'), ('Gyeongsang', '경상'), ('Jeju', '제주')], max_length=100, verbose_name='지역')),
                ('seoul_city', models.CharField(choices=[('Gangnam', '강남구'), ('Songpa', '송파구'), ('Seocho', '서초구'), ('Gangdong', '강동구'), ('Gwanak', '관악구'), ('Yeongdeung', '영등포구'), ('Gangseo', '강서구'), ('Yangcheon', '양천구'), ('Guro', '구로구'), ('Geumcheon', '금천구'), ('Jongno', '종로구'), ('Jung', '중구'), ('Dongdaemun', '동대문구'), ('Jungrang', '중랑구'), ('Mapo', '마포구'), ('Yongsan', '용산구'), ('Seongdong', '성동구'), ('Gwangjin', '광진구'), ('Eunpyeong', '은평구'), ('Seodaemun', '서대문구'), ('Seongbuk', '성북구'), ('Gangbuk', '강북구'), ('Dobong', '도봉구'), ('Nowon', '노원구')], max_length=100, verbose_name='구')),
                ('theme', models.CharField(choices=[('BUSKING', '버스킹'), ('FLEE', '플리마켓'), ('EXHIBITION', '전시회')], max_length=100, verbose_name='테마')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Member')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Creator')),
            ],
        ),
        migrations.AddField(
            model_name='creator',
            name='member',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='login.Member'),
        ),
    ]
