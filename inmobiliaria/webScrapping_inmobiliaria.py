
import libs
from bs4 import BeautifulSoup
from bs4.element import Tag
import json

"""
    En este programa de ejemplo, obtendremos la tabla de viviendas con nuym. habitaciones, superficie y precio

"""

URL = 'https://www.idealista.com/venta-viviendas/barcelona-barcelona/'
PARSER = 'html.parser'
JSON_PATH = './pisos_barcelona.json'
# Creo la instnaic del UrlGetter que usaremos para obtener la diferentes urls

urlGetter = libs.URLGetter()

""" 
    Observando la web, veo que el titulo del piso se diferencia por el tag article:


     <article class="item item_contains_branding full-visibility extended-item item-multimedia-container" data-element-id="107622649" data-online-booking="false">
        <picture class="item-multimedia">
        <div class="item-multimedia-pictures">
        <span>1/</span><span>27</span>
        </div>
        <div class="item-ribbon-container">
        </div>
        <div class="item-gallery gallery-height-core-vitals neutral-orientation">
        <div class="mask-wrapper is-clickable">
        <div class="mask" style="touch-action: pan-y; user-select: none; -webkit-user-drag: none; -webkit-tap-highlight-color: rgba(0, 0, 0, 0); transition-duration: 0s; transform: translateX(0px);">
        <div class="placeholder" style="transform: translateX(-100%);"></div>
        <div class="placeholder" style="transform: translateX(0px);">
        <picture>
        <source height="420" srcset="https://img4.idealista.com/blur/591_420_mq/0/id.pro.es.image.master/41/d9/0b/1317899380.webp" type="image/webp" width="591"/>
        <source height="420" srcset="https://img4.idealista.com/blur/591_420_mq/0/id.pro.es.image.master/41/d9/0b/1317899380.jpg" type="image/jpeg" width="591"/>
        <img alt="Primera foto del inmueble" height="420" loading="lazy" src="https://img4.idealista.com/blur/591_420_mq/0/id.pro.es.image.master/41/d9/0b/1317899380.jpg" style="visibility: visible;" width="591"/>
        </picture>
        </div>
        <div class="placeholder" style="transform: translateX(100%);"></div>
        </div>
        </div>
        </div>
        <section class="item-multimedia-minipictures">
        <figure class="item-multimedia-minipictures--second-image icon-no-pics-outline" data-position="1" data-type="PICTURE">
        <picture>
        <source height="120" srcset="https://img4.idealista.com/blur/189_120_mq/0/id.pro.es.image.master/07/32/30/1317899381.webp" type="image/webp" width="189"/>
        <source height="120" srcset="https://img4.idealista.com/blur/189_120_mq/0/id.pro.es.image.master/07/32/30/1317899381.jpg" type="image/jpeg" width="189"/>
        <img alt="Salón" height="120" loading="lazy" src="https://img4.idealista.com/blur/189_120_mq/0/id.pro.es.image.master/07/32/30/1317899381.jpg" width="189"/>
        </picture>
        </figure>
        <figure class="item-multimedia-minipictures--third-image icon-no-pics-outline" data-position="2" data-type="PICTURE">
        <picture>
        <source height="120" srcset="https://img4.idealista.com/blur/189_120_mq/0/id.pro.es.image.master/b5/2b/40/1317899382.webp" type="image/webp" width="189"/>
        <source height="120" srcset="https://img4.idealista.com/blur/189_120_mq/0/id.pro.es.image.master/b5/2b/40/1317899382.jpg" type="image/jpeg" width="189"/>
        <img alt="Salón" height="120" loading="lazy" src="https://img4.idealista.com/blur/189_120_mq/0/id.pro.es.image.master/b5/2b/40/1317899382.jpg" width="189"/>
        </picture>
        </figure>
        <figure class="item-multimedia-minipictures--plan icon-no-plan" data-type="PLAN">
        <picture>
        <source height="120" srcset="https://img4.idealista.com/blur/189_120_mq/0/id.pro.es.image.master/d1/06/8d/1317899409.webp" type="image/webp" width="189"/>
        <source height="120" srcset="https://img4.idealista.com/blur/189_120_mq/0/id.pro.es.image.master/d1/06/8d/1317899409.jpg" type="image/jpeg" width="189"/>
        <img alt="Plano" height="120" loading="lazy" src="https://img4.idealista.com/blur/189_120_mq/0/id.pro.es.image.master/d1/06/8d/1317899409.jpg" width="189"/>
        </picture>
        </figure>
        </section>
        <div class="item-multimedia-shortcuts">
        <button aria-label="Abrir plano" class="multimedia-shortcut icon-plan" data-button-type="PLAN"></button>
        <button aria-label="Abrir visita 3D" class="multimedia-shortcut icon-3d-tour-outline" data-button-type="VIRTUAL_TOUR_3D"></button>
        <button aria-label="Abrir home staging" class="multimedia-shortcut icon-homestaging" data-button-type="HOME_STAGING"></button>
        <button aria-label="Abrir video" class="multimedia-shortcut icon-video-outline" data-button-type="VIDEO"></button>
        <button aria-label="Abrir mapa" class="multimedia-shortcut icon-location-outline" data-button-type="MAP"></button>
        </div>
        </picture>
        <div class="item-info-container">
        <div class="featured-hightop-block-agent-container">
        <picture class="logo-branding">
        <a data-markup="listado::logo-agencia" href="/pro/engel-volkers-barcelona/" title="Engel &amp; Völkers Barcelona">
        <img alt="Engel &amp; Völkers Barcelona" src="https://st3.idealista.com/d3/de/38/engel-volkers-barcelona.gif"/>
        </a>
        </picture>
        <div class="hightop-agent">
        <a href="/pro/engel-volkers-barcelona/">
        <span class="hightop-kind-agent">Comercializa</span>
        <span class="hightop-agent-name">Engel &amp; Völkers Barcelona</span>
        </a>
        </div>
        </div>
        <a aria-level="2" class="item-link" href="/inmueble/107622649/" role="heading" title="Piso en calle de Pau Claris, La Dreta de l'Eixample, Barcelona">
        Piso en calle de Pau Claris, La Dreta de l'Eixample, Barcelona
        </a>
        <div class="price-row">
        <span class="item-price h2-simulated">1.960.000<span class="txt-big">€</span></span>
        <span class="pricedown">
        <span class="pricedown_price">
        2.150.000 €
        </span>
        <span class="pricedown_icon icon-pricedown">9%</span>
        </span>
        </div>
        <div class="item-detail-char">
        <span class="item-detail">3 hab.</span>
        <span class="item-detail">162 m²</span>
        <span class="item-detail">Planta 3ª exterior con ascensor</span>
        </div>
        <div class="item-description description"><p class="ellipsis">
        Exclusivo piso reformado en Eixample Dret
        Presentamos este exclusivo atico, situado en una finca regia en Eixample Dret, entre Pau Claris y Passeig de Gràcia, a 2 calles de Plaça Catalunya. Este piso de lujo es único y está ubicado en quinto piso real, en la última planta del edificio del año 1931. El edificio construido en 1900 cuenta con 1 ascensor moderno y una bonita entrada señorial. La finca tiene una terraza común en la azotea con unas impresionantes vistas. Su superficie es de 161 metros cuadrados, presume de 7 ventanas con balcones a l
        </p></div>
        <div class="listing-tags-container">
        <span class="listing-tags">Lujo</span>
        </div>
        <div class="item-toolbar item-toolbar--with-border">
        <button class="icon-chat email-btn action-email fake-anchor" type="button"><span>Contactar</span></button>
        <button aria-label="contact phone" class="icon-phone-outline phone-btn hidden-contact-phones_link item-clickable-phone fake-anchor" type="button">
        <span class="hidden-contact-phones_text">Llamar</span>
        <span class="animation_circle">
        <span class="circle"></span>
        <span class="circle"></span>
        <span class="circle"></span>
        </span>
        </button>
        <button aria-label="contact phone" class="icon-phone-outline hidden-contact-phones_link see-phones-btn fake-anchor" type="button">
        <span class="hidden-contact-phones_text">Ver teléfono</span>
        <span class="animation_circle">
        <span class="circle"></span>
        <span class="circle"></span>
        <span class="circle"></span>
        </span>
        </button>
        <button class="trash-btn icon-trash-outline action-discard fake-anchor" data-role="add" data-text-remove="Descartar" rel="nofollow" title="Descartar" type="button">
        <span>Descartar</span>
        </button>
        <button class="icon-no-fav favorite-btn action-fav fake-anchor" data-role="add" data-text-add="Guardar" data-text-remove="Favorito" title="Guardar" type="button">
        <span>Guardar</span>
        </button>
        </div>
        </div>
        <div class="fav-and-lists"></div>
        </article>

    así que lo podemos sacar con el tag article


"""

""" 
    Para soportar la paginacióñn, veo que la web lo que hace es que cuando no encuentra una url, nos envia un 302 a la pagina de inicio.
"""
pisos = []
for i in range(1000):
    # La pagina-1 no exise, es la pasgina base por lo que lo diferencio con un if
    if i == 0:
        url = URL
    else:
        url = URL + 'pagina-' +str(i + 1)+ '.htm'
    print(f"Tratando URL: {url} ...")
    try:
        html = urlGetter.get(url = url)
    except libs.NetworkException as error:
            print(f"ERROR al descargar la url: {error}")
            exit (1)
    if (html.code != 200):
            print(f"FIN descargas")
            break
    bs = BeautifulSoup(html, PARSER)
    pisos_html = bs.find_all('article')
    for piso_html in pisos_html:
        descripcion_str = ''
        loc_str = ''
        price_str = ''
        num_habs = ''
        localizacion = piso_html.find('a', {'class' : 'item-link'})
        superficie = ''
        # Si no hay descripcion es que no es un piso ( article lo usa par mas cosas)
        if localizacion is None:
            continue
        loc_str = localizacion['title']
        price_str = piso_html.find('span', {'class' : 'item-price'}).get_text()
        caracteristicas = piso_html.find_all('div',{'class' : 'item-detail-char'})
        """
            Las caracteristiacs siempre son iguales:
                num. habitaciones
                superficie
                descripcion
            Así que iteramos una a una.
        """
        for i, caracteristica in enumerate(caracteristicas[0].children):
            # Vigila , xq la web tiene un tag con el span y el valor y un navigable string vacio, por lo que los impoares son los que me interesan.
            if (i %2 == 1 and type(caracteristica) == Tag):
                if i == 1:
                    num_habs = caracteristica.get_text()
                    continue
                if i == 3:
                    superficie = caracteristica.get_text()
                    continue
                if i == 5:
                    descripcion_str = caracteristica.get_text()
                    continue
        piso = libs.Piso(
                localizacion = loc_str,
                descripcion = descripcion_str,
                precio = price_str,
                superficie =superficie,
                num_habs = num_habs
            )
        pisos.append(piso)


# Ahora nos queda hacer un export a json
vect_pisos = []
for i, piso in enumerate(pisos):
    dictionary = piso.to_dict()
    vect_pisos.append(dictionary)
pisos_json =  json.dumps(vect_pisos)
with open(JSON_PATH, mode = 'w') as f:
    f.write(pisos_json)
