<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="Yatube_project_0"></a>Yatube project</h1>
<h2 class="code-line" data-line-start=2 data-line-end=3 ><a id="_2"></a>Описание</h2>
<p class="has-line-data" data-line-start="3" data-line-end="9">Создано и зарегистрировано приложение <strong>Posts</strong>.<br>
Подключена база данных.<br>
На главной странице выводятся посление 10 записей.<br>
<br>
Сообщества создает администратор сайта.<br>
<h4 class="code-line" data-line-start=10 data-line-end=11 ><a id="__10"></a>Свойства публикации</h4>
<p class="has-line-data" data-line-start="11" data-line-end="16"> <strong>pk</strong> - уникальный номер публикации;<br>
<strong>text</strong> - текст публикации;<br>
<strong>pub_date</strong> - дата публикации (день, меяц, год);<br>
<strong>author</strong> - автор (ссылка на модель User (связь «один-ко-многим»));<br>
<strong>group</strong> - название сообщества, в котором находится публикация (ссылка на модель Group (связь «один-ко-многим»)).</p>
<h4 class="code-line" data-line-start=17 data-line-end=18 ><a id="__17"></a>Свойства сообщества</h4>
<p class="has-line-data" data-line-start="18" data-line-end="21"><strong>title</strong> - название сообщества;<br>
<strong>slug</strong> - уникальный адрес сообщества;<br>
<strong>description</strong> - описание сообщества.</p>
<h4 class="code-line" data-line-start=22 data-line-end=23 ><a id="_22"></a>Реализовано</h4>
<p class="has-line-data" data-line-start="23" data-line-end="34">Создана модель сообщества с названием <strong>Group</strong>. В ней указан метод <em>str</em>, чтобы при печати объекта на экран выводилось поле <em>title</em>.<br>
В модель <strong>Post</strong> добавлено свойство <em>group</em>, чтобы при добавлении новой записи можно было сослаться на группу (<strong>Group</strong>).<br>
Создана view-функция <em>index</em>, она передаёт в шаблон <em>posts/index.html</em>  10 последних объектов модели <strong>Post</strong>.<br>
Создана view-функция <em>group_posts</em>, она опередаёт в шаблон <em>posts/group_list.html</em> 10 последних объектов модели <strong>Post</strong>, отфильтрованных по полю <em>group</em>, и содержимое для тега <em>&lt;title&gt;</em>. Адрес страницы сообщества - <em>/group/slug/</em>. Если адрес сообщества не найден, выводится код ошибки 404.<br>
Подготовлены шаблоны:<br>
<strong>base.html</strong> - базовый шаблон;<br>
<strong>header.html</strong> - шаблон заголовка;<br>
<strong>footer.html</strong> - шаблон нижнего колонтитула;<br>
<strong>index.html</strong> - шаблон для главной страницы;<br>
<strong>group_list.html</strong> - шаблон для сообщества.<br>
<h2 class="code-line" data-line-start=35 data-line-end=36 ><a id="_35"></a>Технологии</h2>
<p class="has-line-data" data-line-start="36" data-line-end="38">Python 3.9.14<br>
 Django 2.2.19</p>
<h2 class="code-line" data-line-start=39 data-line-end=40 ><a id="___dev_39"></a>Запуск проекта в dev-режиме</h2>
<h4 class="code-line" data-line-start=40 data-line-end=41 ><a id="1______40"></a>1️ Установите и активируйте виртуальное окружение</h4>
<p class="has-line-data" data-line-start="41" data-line-end="42">Установите виртуальное окружение: в терминале перейдите в корневую директорию проекта и выполните команду:</p>
<ul>
<li class="has-line-data" data-line-start="42" data-line-end="43"><em>в Windows:</em></li>
</ul>
<pre><code class="has-line-data" data-line-start="44" data-line-end="46">python -m venv venv
</code></pre>
<ul>
<li class="has-line-data" data-line-start="46" data-line-end="47"><em>в macOS или Linux:</em></li>
</ul>
<pre><code class="has-line-data" data-line-start="48" data-line-end="50">python3 -m venv venv
</code></pre>
<p class="has-line-data" data-line-start="50" data-line-end="51">Запустите виртуальное окружение с помощью команды:</p>
<ul>
<li class="has-line-data" data-line-start="51" data-line-end="52"><em>в Windows:</em></li>
</ul>
<pre><code class="has-line-data" data-line-start="53" data-line-end="55">source venv/Scripts/activate
</code></pre>
<ul>
<li class="has-line-data" data-line-start="55" data-line-end="56"><em>в macOS или Linux:</em></li>
</ul>
<pre><code class="has-line-data" data-line-start="57" data-line-end="59">source venv/bin/activate
</code></pre>
<h4 class="code-line" data-line-start=59 data-line-end=60 ><a id="2_____requirementstxt_59"></a>2️ Установите зависимости из файла requirements.txt</h4>
<pre><code class="has-line-data" data-line-start="61" data-line-end="63">pip install -r requirements.txt
</code></pre>
<h4 class="code-line" data-line-start=63 data-line-end=64 ><a id="3________63"></a>3️ Выполните команду, запускающую сервер в режиме разработки:</h4>
<p class="has-line-data" data-line-start="64" data-line-end="65">В папке с файлом <a href="http://manage.py">manage.py</a> выполните команду:</p>
<ul>
<li class="has-line-data" data-line-start="65" data-line-end="66"><em>в Windows:</em></li>
</ul>
<pre><code class="has-line-data" data-line-start="67" data-line-end="69">python manage.py runserver
</code></pre>
<ul>
<li class="has-line-data" data-line-start="69" data-line-end="70"><em>в macOS или Linux:</em></li>
</ul>
<pre><code class="has-line-data" data-line-start="71" data-line-end="73">python3 manage.py runserver
</code></pre>
Игорь Чиж
