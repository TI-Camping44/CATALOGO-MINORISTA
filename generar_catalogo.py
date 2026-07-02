import xmlrpc.client
import os
import json

# =====================================
# CONFIGURACIÓN DIRECTA (CAMPING 44)
# =====================================
URL = "https://camping44.odoo.com"
DB = "gcaceres93-camping-main-15845610"
USER = "facundocolman@camping44.com.py"
API_KEY = "55f70e57a3caa3113e3ffa559b5ba020931dc501"

# LISTA MAESTRA DE SKUs EN LIQUIDACIÓN (PROVISTA POR EL DIRECTORIO)
SKUS_LIQUIDACION = set(
    "110306 110307 110509 110562 110563 110567 110568 110569 110582 110583 110584 110585 110586 110587 110588 110589 110734 110738 110739 110751 110753 110756 110759 110760 111564 111566 112000 115702 115703 115704 140470 140704 140705 140706 140707 151500 151501 151502 151516 151523 151531 151537 151538 151539 151543 151544 151565 151570 151590 151595 151661 160082 170229 170356 190001 200137 200138 200139 200320 200378 250060 250061 250062 250690 250691 250692 250693 250694 260252 260275 260357 260360 260361 260362 260366 260368 260372 260375 260601 260715 260850 261300 261405 261406 262000 270050 270056 270057 270101 270103 270150 270151 270151U 270152 270157 270198 270200 270202 270203 270204 270204U 270250 270251 270500 270501 270550 270560 270565 270570 270575 270601 270602 270650 270660 270680 270689 270801 270808 270809 270812 270813 270816 270821 270822 270823 270830 270900 272022 272063 300090 300091 300092 300093 300094 300096 320016 320054 320061 320065 320079 320095 320130 320155 320156 320202 320207 320259 320280EGF 320400 320514 320515 320516 320517 320600 321055 321057 321058 321060 321061 321062 321070 321075 323110 323510 324000 324020 350200 350201 350202 350203 400212 400214 400216 400217 400221 400231 400247 400253 400290 400291 400386 440154 440158 440161 440162 510260 510261 510262 510749 550259 550400 610914 610927 610932 610935 610936 610937 610939 610941 610945 610946 610947 610948 610950 610966 610967 610968 610979 610980 611254 620122 620123 620182 620184 620189 620193 620202 620580 620581 620582 620583 620584 620585 620586 620587 620588 620589 620590 620591 620600 620601 620602 620603 620604 620605 620606 620607 620608 620609 620610 620611 620612 620613 620615 620616 620617 620618 620619 620620 620621 620622 620623 620624 620625 620626 620627 620628 620629 620630 620631 620632 620633 620634 620644 620646 620648 620649 620650 620651 620653 620655 620656 620657 620658 620659 620660 620661 620662 620663 620664 620665 620666 620667 620668 620670 620672 620673 620674 620676 620677 620679 620680 620681 620682 620683 620684 620685 620686 620687 620688 620689 620690 620691 620692 620693 620694 620695 620696 620697 620698 620699 621010 621011 621013 621022 621040 621041 621042 621043 621044 621046 621050 621054 621058 621062 621070 621071 621072 621073 621076 621080 621084 621100 621101 621102 621103 621104 621105 621106 621107 621108 621109 621110 621111 621112 621114 621115 621116 621117 621118 621119 621120 621121 621122 621123 621124 621125 621126 621127 621128 621129 621130 621131 621132 621150 621151 621152 621153 621154 621155 621156 621200 621201 621202 621203 621204 621205 621206 621207 621208 621209 621210 621214 621218 621222 630030 630031 630032 630033 630034 630035 630036 630037 630038 630039 630040 670113 680085 680466 680477 680532 680534 680537 680539 680552 680564 680571 680572 680592 680597 680598 680599 680675 680848 680850 681090 681100 681100EGF 681101 681102 681103 681104 681105 681105EGF 681106 681107 681108 681109 681110 681111 681112 681113 681115 681116 681120 681122 710418 711300 711305 711307 712115 712116 712117 712118 712120 730459 749000 751000 751002 751003 751004 751005 751007 751008 751009 751010 760060 770522 800170 800173 830240 830241 830242 830243 830246 830247 830249 830250 830251 830252 830253 830254 830255 830256 830257 830258 830259 830260 830261 830262 830263 830264 830265 830266 830267 830268 830269 830270 830273 830276 830277 830278 830280 830281 830282 830283 830284 830285 830286 830287 830288 830290 830291 830293 830294 830295 830296 830313 830314 830318 830319 830322 830323 830324 830325 830327 830328 830329 830334 830335 830337 830340 830342 830345 830346 830350 830351 830352 830353 830354 830355 830356 830357 830358 900376 900379 900382 900383 900397 900398 900621 900806 900810 901001 901005 901010 901150 901152 901265 901273 901408 901410 901411 901412 901500 901600 901601 901610 901611 901620 901621 904000 904100 920120 920140 920141 920142 920143 920146 920147 920150 920184 920392 920394 920398 920414 920415 920420 921063 921140 940178 940179 990060 DES149010 DES150080 DES151202 DES151562 DES151563 DES151564 DES151611 DES151612 DES190001 DES191100 DES191110 DES320154 DES320202 DES320207 DES320259 DES320270 DES320275 DES320522 DES320850 DES321201 DES321202 DES321203 DES323500 DES325000 DES400258 DES440220 DES510130 DES611034 DES650225 DES680467 DES680470 DES680507 DES680509 DES680512 DES680513 DES680514 DES680516 DES680517 DES680518 DES680525 DES680529 DES680531 DES680532 DES680537 DES680539 DES680540 DES680549 DES680552 DES680554 DES680557 DES680561 DES681101 DES710031 DES710240 DES710422 DES750100 DES750185 DES750186 DES750190 DES750300 DES750301 DES750302 DES750305 DES750310 DES750315 DES750325 DES750330 DES750335 DES750340 DES750420 DES750422 DES750427 DES750428 DES750429 DES770700 DES880051 DES880052 DES880053 DES880054 DES880055 DES880070 DES880071 DES880072 DES880073 DES880074 DES880075 DES880091 DES880092 DES901152 DES901411 DES920155 DES920284 DES941058 DES941059 EGF320007 LIQ150970 LIQ150982 LIQ150983 LIQ150985 LIQ150995 LIQ150996 LIQ151190 LIQ170135 LIQ260048 LIQ260276 LIQ260560 LIQ320019 LIQ320069 LIQ320156 LIQ320202 LIQ320260 LIQ320264 LIQ320445 LIQ320450 LIQ320511 LIQ320800 LIQ320850 LIQ321000 LIQ322500 LIQ324100 LIQ610902 LIQ610962 LIQ610964 LIQ680465 LIQ680554 LIQ680555 LIQ680558 LIQ680595 LIQ680597 LIQ680598 LIQ680599 LIQ680670 LIQ710031 LIQ750301 LIQ750330 LIQ750428 LIQ750429 LIQ770301 LIQ800160 LIQ800170 LIQ800173 LIQ800175 LIQ800186 LIQ800190 LIQ920110 LIQREP611063 LIQREP900770 LIQREP900772 LIQREP900773 REP900300 REP900301 REP900302 REP900767 REP900768 REP900769 REP900775 REP900776 REP900777 REP900778 REP900779 REP900780 REP900781 REP900782 REP900783 REP900784 REP900785 REP900786 REP900787 REP900788 REP900789 REP900791 REP900792 REP900793 REP900795 REP900798 REP900803 REP900853 REP900866 REP900867 REP900868 REP900869 REP901100 REP901120 REP901130 REP901140".split()
)

def main():
    try:
        common = xmlrpc.client.ServerProxy(f'{URL}/xmlrpc/2/common')
        uid = common.authenticate(DB, USER, API_KEY, {})
        models = xmlrpc.client.ServerProxy(f'{URL}/xmlrpc/2/object')

        print("Conectado a Odoo exitosamente. Extrayendo datos de la empresa...")

        comp_data = models.execute_kw(DB, uid, API_KEY, 'res.company', 'search_read', [[['id', '=', 1]]], {'fields': ['logo_web']})
        logo_base64 = ""
        if comp_data and comp_data[0].get('logo_web'):
            logo_base64 = comp_data[0]['logo_web']
            if isinstance(logo_base64, bytes):
                logo_base64 = logo_base64.decode('utf-8')

        pl_data = models.execute_kw(DB, uid, API_KEY, 'product.pricelist', 'search_read',
            [[['company_id', '=', 1]]], {'fields': ['id', 'name'], 'limit': 500})
        
        listas_excluir = ["DIA CONTI", "ALSK-ALQUILER DE OFICINA", "PROMO", "MAYS USD", "CRE USD", "DIST1 USD", "DIST2 USD", "SAL USD"]
        pricelists = []
        usados = set()

        for pl in pl_data:
            nombre = (pl.get('name') or "").upper().strip()
            if nombre in listas_excluir: continue
            if nombre == "DIST1": nombre = "DIST 1"
            if nombre == "DIST2": nombre = "DIST 2"
            
            if nombre not in usados:
                usados.add(nombre)
                pl['name_clean'] = nombre
                pricelists.append(pl)

        orden_precios = ["CONGS", "DIST 1", "DIST 2", "CREGS", "MAYGS", "SALGS"]
        pricelists.sort(key=lambda x: orden_precios.index(x['name_clean']) if x['name_clean'] in orden_precios else 999)

        print("Extrayendo items de listas de precios...")
        pl_items = models.execute_kw(DB, uid, API_KEY, 'product.pricelist.item', 'search_read',
            [[]], {'fields': ['pricelist_id', 'product_tmpl_id', 'fixed_price'], 'limit': 50000})

        mapa_precios = {}
        for item in pl_items:
            tmpl_id = item['product_tmpl_id'][0] if item.get('product_tmpl_id') else None
            pl_id = item['pricelist_id'][0] if item.get('pricelist_id') else None
            if tmpl_id and pl_id:
                if tmpl_id not in mapa_precios: mapa_precios[tmpl_id] = {}
                mapa_precios[tmpl_id][pl_id] = item.get('fixed_price', 0.0)

        print("Extrayendo productos de Odoo...")
        filtros = [['sale_ok', '=', True], ['active', '=', True], ['company_id', '=', 1]]
        campos = ['id', 'name', 'default_code', 'qty_available', 'categ_id', 'product_brand_id', 'product_tmpl_id', 'image_128']
        products = models.execute_kw(DB, uid, API_KEY, 'product.product', 'search_read', [filtros], {'fields': campos, 'limit': 50000})

        print("Descontando productos perdidos (Ubicación NSE)...")
        nse_locs = models.execute_kw(DB, uid, API_KEY, 'stock.location', 'search', [[['complete_name', 'ilike', 'NSE']]])
        nse_stock = {}
        
        if nse_locs:
            quants = models.execute_kw(DB, uid, API_KEY, 'stock.quant', 'search_read', 
                [[['location_id', 'in', nse_locs]]], 
                {'fields': ['product_id', 'quantity']})
                
            for q in quants:
                if q.get('product_id'):
                    pid = q['product_id'][0] if isinstance(q['product_id'], list) else q['product_id']
                    nse_stock[pid] = nse_stock.get(pid, 0.0) + float(q.get('quantity', 0.0))

        categorias_datos = {}
        orden_hojas = [
            "Todo", "🔥 LIQUIDACIÓN", "Municiones", "Armas", "Cargadores", "ASG", "TSS", "CROSMAN", "UMAREX",
            "DOBERMAN RIFLES", "DOBERMAN MOCHILAS", "DOBERMAN BOTAS", "DOBERMAN LINTERNAS", "DOBERMAN BALINES",
            "VECTOR OPTICS", "KONUS", "BWC", "TRUGLO", "MIGUEL NIETO", "NTK", "COLEMAN", "IMALENT",
            "APOLO", "AITOR", "ROCKY BOOTS", "KCI", "NITECORE", "CATERPILLAR", "POLYMER", "SNAKE",
            "FOBUS", "BERETTA MOD", "B.E ARMOR", "OTRO"
        ]
        for hoja in orden_hojas: categorias_datos[hoja] = []

        print("Filtrando catálogo minorista...")
        for p in products:
            ref = (p.get('default_code') or "").upper().strip()
            if ref.startswith("AVE") or ref.startswith("NSE") or ref.startswith("INT"): continue

            categoria_str = p['categ_id'][1].upper() if p.get('categ_id') else ""
            desc = (p.get('name') or "").upper()
            
            palabras_bloqueadas = ["VITALICA", "RRHH", "UNIFORME", "SERVICIO TECNICO", "GASTO", "CONSUMO INTERNO", "ACTIVO FIJO", "OFICINA"]
            if any(pb in categoria_str or pb in desc for pb in palabras_bloqueadas): continue

            stock = float(p.get('qty_available') or 0.0)
            if p['id'] in nse_stock: stock = stock - nse_stock[p['id']]
            if stock <= 0: continue

            tmpl_id = p['product_tmpl_id'][0] if p.get('product_tmpl_id') else 0
            marca_str = p['product_brand_id'][1].upper() if p.get('product_brand_id') else "SIN MARCA"

            es_liquidacion = ref in SKUS_LIQUIDACION or any(palabra in categoria_str or palabra in desc for palabra in ["LIQUIDACION", "LIQUIDACIÓN", "OUTLET"])

            hoja = "OTRO"
            if es_liquidacion: hoja = "🔥 LIQUIDACIÓN"
            elif "MUNICION" in categoria_str: hoja = "Municiones"
            elif "ARMA" in categoria_str and "ACCESORIO" not in categoria_str: hoja = "Armas"
            elif "ASG" in categoria_str or "ASG" in marca_str or "ASG" in desc: hoja = "ASG"
            elif "TSS" in marca_str: hoja = "TSS"
            elif "CROSMAN" in marca_str: hoja = "CROSMAN"
            elif "UMAREX" in marca_str: hoja = "UMAREX"
            elif "VECTOR" in marca_str: hoja = "VECTOR OPTICS"
            elif "KONUS" in marca_str: hoja = "KONUS"
            elif "BWC" in marca_str: hoja = "BWC"
            elif "TRUGLO" in marca_str: hoja = "TRUGLO"
            elif "MIGUEL" in marca_str: hoja = "MIGUEL NIETO"
            elif "NTK" in marca_str: hoja = "NTK"
            elif "COLEMAN" in marca_str: hoja = "COLEMAN"
            elif "IMALENT" in marca_str: hoja = "IMALENT"
            elif "APOLO" in marca_str: hoja = "APOLO"
            elif "AITOR" in marca_str: hoja = "AITOR"
            elif "ROCKY" in marca_str: hoja = "ROCKY BOOTS"
            elif "KCI" in marca_str: hoja = "KCI"
            elif "NITECORE" in marca_str: hoja = "NITECORE"
            elif "CATERPILLAR" in marca_str: hoja = "CATERPILLAR"
            elif "POLYMER" in marca_str: hoja = "POLYMER"
            elif "SNAKE" in marca_str: hoja = "SNAKE"
            elif "FOBUS" in marca_str: hoja = "FOBUS"
            elif "BERETTA" in marca_str: hoja = "BERETTA MOD"
            elif "B.E" in marca_str: hoja = "B.E ARMOR"

            if "DOBERMAN" in marca_str:
                if "RIFLE" in desc: hoja = "DOBERMAN RIFLES"
                if "MOCHIL" in desc: hoja = "DOBERMAN MOCHILAS"
                if "BOTA" in desc: hoja = "DOBERMAN BOTAS"
                if "LINTERNA" in desc: hoja = "DOBERMAN LINTERNAS"
                if "BALIN" in desc: hoja = "DOBERMAN BALINES"

            if "CARGADOR" in desc and not any(x in desc for x in ["PORTA", "BASE", "PISO", "ACOPLE"]) and not es_liquidacion: 
                hoja = "Cargadores"

            p['stock_calculado'] = stock
            p['hoja_asignada'] = hoja
            p['marca_limpia'] = p['product_brand_id'][1] if p.get('product_brand_id') else "Sin Marca"
            
            p_precios = []
            for pl in pricelists:
                p_val = mapa_precios.get(tmpl_id, {}).get(pl['id'], 0.0)
                p_precios.append(p_val)
            p['lista_precios_vals'] = p_precios

            categorias_datos[hoja].append(p)
            categorias_datos["Todo"].append(p)

        print("Separando datos livianos de mapas de imágenes binarias...")
        productos_js = []
        imagenes_js = {} 
        
        for p in categorias_datos["Todo"]:
            base_price = 0.0
            for val in p['lista_precios_vals']:
                if float(val or 0.0) > 0:
                    base_price = float(val)
                    break

            cod_limpio = p.get('default_code', '-').strip()
            prod_dict = {
                "c": cod_limpio,
                "n": p.get('name', ''),
                "m": p['marca_limpia'],
                "s": int(p['stock_calculado']),
                "h": p['hoja_asignada'],
                "pr": base_price,
                "p": {}
            }
            
            img_data = p.get('image_128')
            if img_data:
                if hasattr(img_data, 'data'): img_data = img_data.data
                img_base64 = img_data.decode("utf-8") if isinstance(img_data, bytes) else img_data
                imagenes_js[cod_limpio] = img_base64
                
            for idx, precio in enumerate(p['lista_precios_vals']):
                pl_name = pricelists[idx]["name_clean"]
                precio_val = float(precio or 0.0)
                if precio_val > 0:
                    if "USD" in pl_name:
                        prod_dict["p"][pl_name] = f"US$ {precio_val:,.2f}"
                    else:
                        prod_dict["p"][pl_name] = f"{int(round(precio_val)):,}".replace(",", ".") + " Gs."
                        
            productos_js.append(prod_dict)

        json_str = json.dumps(productos_js)
        json_images_str = json.dumps(imagenes_js)
        logo_html = f"data:image/png;base64,{logo_base64}" if logo_base64 else ""

        print("Generando index.html...")
        
        html = """<!DOCTYPE html><html lang='es'><head><meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1.0'><title>Catálogo Salón - Camping 44</title>
        <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css' rel='stylesheet'>
        <script src='https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js'></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf-autotable/3.5.31/jspdf.plugin.autotable.min.js"></script>
        <style>
            body{background-color:#f4f6f9;font-family:'Segoe UI',sans-serif;padding-bottom:80px;}
            .stock-rojo{background-color:#FEE2E2!important;color:#991B1B;}
            .stock-amarillo{background-color:#FEF3C7!important;color:#92400E;}
            .stock-verde{background-color:#D1FAE5!important;color:#065F46;}
            .desktop-sidebar{position:sticky;top:0;height:100vh;overflow-y:auto;background:#fff;border-right:1px solid #e5e7eb;padding:25px 15px;box-shadow:2px 0 10px rgba(0,0,0,0.03);}
            .btn-filtro{color:#081226;font-size:0.9rem;padding:9px 14px;font-weight:600;border-radius:30px;border:1px solid #dee2e6;text-align:left;width:100%;cursor:pointer;background:#fff;transition:0.2s;margin-bottom:5px;}
            .btn-filtro.active{background-color:#081226;color:white;border-color:#081226;}
            .btn-filtro[data-filtro="🔥 LIQUIDACIÓN"] { color: #dc3545; border-color: #f8d7da; background-color: #fff5f5; }
            .btn-filtro[data-filtro="🔥 LIQUIDACIÓN"].active { background-color: #dc3545; color: white; border-color: #dc3545; }
            
            .btn-tarifa{color:#166534;font-size:0.9rem;padding:8px 12px;font-weight:600;border-radius:30px;border:1px solid #bbf7d0;text-align:left;width:100%;cursor:pointer;background:#f0fdf4;transition:0.2s;margin-bottom:5px;}
            .btn-tarifa.active{background-color:#166534;color:white;border-color:#166534;}
            .pdf-panel{background:#fff;border:1px solid #e5e7eb;border-radius:14px;padding:15px;display:flex;flex-wrap:wrap;gap:15px;align-items:center;justify-content:space-between;}
            .pdf-panel-title{font-size:0.85rem;font-weight:800;color:#dc3545;margin:0;}
            .check-group{display:flex;flex-wrap:wrap;gap:12px;align-items:center;}
            .tarjeta-contenedor{contain: content;}
            .producto-img{width:100%;height:140px;object-fit:contain;background:white;padding:5px;}
            @media(min-width:768px){.producto-img{height:185px;}}
            .card-producto{border-radius:14px;overflow:hidden;background:#fff;border:1px solid #e5e7eb;height:100%;transition:transform 0.15s;}
            .price-box{background:#f9fafb;border-radius:8px;padding:5px;font-size:0.75rem;text-align:center;border:1px solid #e5e7eb;height:100%;display:flex;flex-direction:column;justify-content:center;}
            .zona-seguridad{display:none;}
            .mobile-header{background:#fff;border-bottom:1px solid #e5e7eb;position:sticky;top:0;z-index:1020;padding:12px 20px;}
            .btn-floating-menu{position:fixed;bottom:20px;right:20px;z-index:1030;background:#081226;color:#fff;border:none;padding:14px 28px;border-radius:30px;font-weight:bold;box-shadow:0 4px 15px rgba(0,0,0,0.25);}
            @media print{#web-app{display:none!important;}#print-placeholder{display:block!important;width:100%;}.print-table{width:100%!important;border-collapse:collapse!important;margin-top:20px;}.print-table th{background-color:#081226!important;color:white!important;padding:8px;font-size:11px;text-align:center;}.print-table td{padding:6px;border:1px solid #ddd;font-size:11px;vertical-align:middle;}}
        </style></head><body><div id="web-app">
        
        <div class="mobile-header d-flex justify-content-between align-items-center d-lg-none shadow-sm">
            <img src="##LOGO_HTML##" alt="Logo" style="height:55px; object-fit:contain; max-width:180px;">
            <button class="btn btn-sm btn-danger fw-bold rounded-pill px-3" onclick="toggleModoSeguridad()" id="btnToggleSeguridadMob">🔓 Seguridad</button>
        </div>

        <button class="btn-floating-menu d-lg-none shadow" data-bs-toggle="offcanvas" data-bs-target="#sidebarOffcanvas">📦 Categorías / Marcas</button>

        <div class="offcanvas offcanvas-start" id="sidebarOffcanvas" style="width:280px;">
            <div class="offcanvas-header border-bottom">
                <h5 class="offcanvas-title fw-bold">Filtros de Catálogo</h5>
                <button type="button" class="btn-close" data-bs-dismiss="offcanvas"></button>
            </div>
            <div class="offcanvas-body bg-light" id="contenedorFiltrosMovil"></div>
        </div>

        <div class='container-fluid'><div class='row'>
        
        <div class='col-lg-2 d-none d-lg-block desktop-sidebar' id="sidebarDesktop">
            <div class='text-center mb-3'><img src='##LOGO_HTML##' alt='Logo' style='height:75px;max-width:100%;object-fit:contain;'><h5 class='fw-bold mt-2 text-dark' style="font-size:1.05rem;">Catálogo de Salón</h5></div>
            <button id="btnToggleSeguridad" class="btn btn-outline-danger btn-sm w-100 fw-bold rounded-pill mb-3" onclick="toggleModoSeguridad()">🔓 Modo Clientes Seguridad</button>
            <div id="seccionFiltrosMaster">
                <h6 class='fw-bold mb-2 text-success px-1' style='font-size:0.8rem;'>1. TARIFA EN PANTALLA</h6>
                <ul class='nav flex-column gap-1 mb-3'>
                    <li class='nav-item'><button class='btn-tarifa active' data-tarifa='Todas'>👁️ Mostrar Todas</button></li>
                    <li class='nav-item'><button class='btn-tarifa' data-tarifa='SALGS'>💲 Tarifa SALGS (Salón)</button></li>
                    <li class='nav-item zona-seguridad'><button class='btn-tarifa' data-tarifa='MAYGS'>🛡️ Tarifa MAYGS</button></li>
                    <li class='nav-item zona-seguridad'><button class='btn-tarifa' data-tarifa='DIST 1'>🛡️ Tarifa DIST 1</button></li>
                    <li class='nav-item zona-seguridad'><button class='btn-tarifa' data-tarifa='DIST 2'>🛡️ Tarifa DIST 2</button></li>
                    <li class='nav-item zona-seguridad'><button class='btn-tarifa' data-tarifa='CREGS'>🛡️ Tarifa CREGS</button></li>
                    <li class='nav-item zona-seguridad'><button class='btn-tarifa' data-tarifa='CONGS'>🛡️ Tarifa CONGS</button></li>
                </ul>
                <hr>
                <h6 class='fw-bold mb-2 text-dark px-1' style='font-size:0.8rem;'>2. FILTRAR CATEGORÍA</h6>
                <ul class='nav flex-column gap-1' id="listaCategoriasM">"""
        
        html = html.replace('##LOGO_HTML##', logo_html)
        
        first_tab = True
        for hoja in orden_hojas:
            pandas_clone = categorias_datos[hoja]
            if not pandas_clone and hoja != "Todo": continue
            active_class = "active" if first_tab else ""
            html += f"<li class='nav-item'><button class='btn-filtro {active_class}' data-filtro='{hoja}'>📦 {hoja} ({len(pandas_clone)})</button></li>"
            first_tab = False

        html += """</ul></div></div>
        
        <div class='col-12 col-lg-10 py-3'>
            <div class='row g-2 mb-3'>
                <div class='col-12 col-md-8'><input type='text' id='buscadorWeb' class='form-control form-control-lg border-2 shadow-sm rounded-pill px-4' placeholder='🔍 Escribe código o nombre para buscar...'></div>
                <div class='col-12 col-md-4'><select id='ordenarPor' class='form-select form-select-lg border-2 shadow-sm rounded-pill'><option value='default'>⇅ Ordenar por...</option><option value='az'>🔤 A - Z (Alfabético)</option><option value='za'>🔤 Z - A (Alfabético)</option><option value='stock_desc'>📦 Mayor Stock</option><option value='stock_asc'>📦 Menor Stock</option><option value='precio_asc'>💲 Menor Precio</option><option value='precio_desc'>💲 Mayor Precio</option></select></div>
            </div>
            
            <div class='pdf-panel shadow-sm mb-3'>
                <div class='check-group'>
                    <span class='pdf-panel-title'>📄 COTIZACIÓN PDF:</span>
                    <div class='form-check form-check-inline m-0'><input class='form-check-input check-tarifa-pdf' type='checkbox' value='SALGS' id='chk_SALGS' checked><label class='form-check-label fw-bold text-dark' for='chk_SALGS'>SALGS</label></div>
                    <div class='form-check form-check-inline m-0 zona-seguridad'><input class='form-check-input check-tarifa-pdf' type='checkbox' value='MAYGS' id='chk_MAYGS'><label class='form-check-label fw-bold text-danger' for='chk_MAYGS'>MAYGS</label></div>
                    <div class='form-check form-check-inline m-0 zona-seguridad'><input class='form-check-input check-tarifa-pdf' type='checkbox' value='DIST 1' id='chk_DIST1'><label class='form-check-label fw-bold text-danger' for='chk_DIST1'>DIST 1</label></div>
                    <div class='form-check form-check-inline m-0 zona-seguridad'><input class='form-check-input check-tarifa-pdf' type='checkbox' value='DIST 2' id='chk_DIST2'><label class='form-check-label fw-bold text-danger' for='chk_DIST2'>DIST 2</label></div>
                    <div class='form-check form-check-inline m-0 border-start ps-2'><input class='form-check-input' type='checkbox' id='chkMostrarStock' checked><label class='form-check-label small text-muted fw-bold' for='chkMostrarStock'>📦 Stock</label></div>
                </div>
                <button id='btnGenerarPDF' onclick='descargarPDFNativo()' class='btn btn-danger btn-sm fw-bold px-4 py-2 rounded-pill shadow-sm'>DESCARGAR PDF</button>
            </div>
            
            <div class='row row-cols-2 row-cols-md-3 row-cols-lg-4 g-2 g-md-3' id='grilla-productos'></div>
        </div>
        
        </div></div></div></div></div><div id='print-placeholder'></div>
        <script>
            let debounceTimer;
            const PRODUCTOS = ##JSON_DATA##;
            const IMAGENES = ##JSON_IMAGES##;
            
            let stateCat = 'Todo'; let stateSearch = ''; let stateTarifa = 'Todas'; let stateSort = 'default';
            let modoSeguridadActivo = false;
            let productosFiltrados = []; let paginaActual = 0; const ITEMS_POR_PAGINA = 30;

            document.getElementById('contenedorFiltrosMovil').innerHTML = document.getElementById('seccionFiltrosMaster').innerHTML;

            // FUNCIÓN MAESTRA PARA CALCULAR LA REBAJA DEL 30% EXACTA EN CLIENTE
            function formatLiquidation(precioStr) {
                if (!precioStr || precioStr === '-') return '-';
                if (precioStr.includes('US$')) {
                    let num = parseFloat(precioStr.replace('US$', '').replace(/,/g, '').trim());
                    return `US$ ${(num * 0.7).toFixed(2)}`;
                } else {
                    let num = parseInt(precioStr.replace('Gs.', '').replace(/\./g, '').trim());
                    return Math.round(num * 0.7).toLocaleString('de-DE') + ' Gs.';
                }
            }

            function toggleModoSeguridad() {
                modoSeguridadActivo = !modoSeguridadActivo;
                document.querySelectorAll('.zona-seguridad').forEach(el => {
                    el.style.display = modoSeguridadActivo ? 'block' : 'none';
                    if(el.tagName === 'DIV' || el.tagName === 'INPUT') el.style.display = modoSeguridadActivo ? 'inline-block' : 'none';
                });
                
                document.getElementById('btnToggleSeguridad').innerHTML = modoSeguridadActivo ? '🔒 Salir Seguridad' : '🔓 Modo Clientes Seguridad';
                document.getElementById('btnToggleSeguridad').className = modoSeguridadActivo ? 'btn btn-success btn-sm w-100 fw-bold rounded-pill mb-3' : 'btn btn-outline-danger btn-sm w-100 fw-bold rounded-pill mb-3';
                document.getElementById('btnToggleSeguridadMob').innerHTML = modoSeguridadActivo ? '🔒 Salir' : '🔓 Seguridad';
                document.getElementById('btnToggleSeguridadMob').className = modoSeguridadActivo ? 'btn btn-sm btn-success fw-bold rounded-pill px-3' : 'btn btn-sm btn-danger fw-bold rounded-pill px-3';
                
                if(!modoSeguridadActivo) {
                    stateTarifa = 'Todas';
                    document.querySelectorAll('.btn-tarifa').forEach(b => b.classList.remove('active'));
                    document.querySelectorAll('.btn-tarifa[data-tarifa="Todas"]').forEach(b => b.classList.add('active'));
                    document.querySelectorAll('.check-tarifa-pdf').forEach(cb => { if(cb.value !== 'SALGS') cb.checked = false; });
                }
                aplicarFiltros();
            }

            function aplicarFiltros() {
                let q = stateSearch.toUpperCase().trim();
                
                productosFiltrados = PRODUCTOS.filter(p => {
                    let matchCat = (stateCat === 'Todo' || p.h === stateCat);
                    let matchSearch = (q === '' || p.n.toUpperCase().includes(q) || p.c.toUpperCase().includes(q));
                    let matchTarifa = stateTarifa === 'Todas' ? true : p.p[stateTarifa] !== undefined;
                    return matchCat && matchSearch && matchTarifa;
                });
                
                if (stateSort==='az') productosFiltrados.sort((a,b)=>a.n.localeCompare(b.n));
                else if (stateSort==='za') productosFiltrados.sort((a,b)=>b.n.localeCompare(a.n));
                else if (stateSort==='stock_desc') productosFiltrados.sort((a,b)=>b.s - a.s);
                else if (stateSort==='stock_asc') productosFiltrados.sort((a,b)=>a.s - b.s);
                else if (stateSort==='precio_asc') productosFiltrados.sort((a,b)=>a.pr - b.pr);
                else if (stateSort==='precio_desc') productosFiltrados.sort((a,b)=>b.pr - a.pr);
                
                paginaActual = 0; 
                document.getElementById('grilla-productos').innerHTML = ''; 
                renderizarPagina();
            }

            document.getElementById('ordenarPor').addEventListener('change', function() { stateSort = this.value; aplicarFiltros(); });

            function renderizarPagina() {
                let start = paginaActual * ITEMS_POR_PAGINA; 
                let end = start + ITEMS_POR_PAGINA;
                let items = productosFiltrados.slice(start, end);
                
                if (items.length === 0 && paginaActual === 0) {
                    document.getElementById('grilla-productos').innerHTML = '<div class="col-12 text-center py-5"><h5 class="text-muted">No se encontraron productos</h5></div>'; return;
                }
                
                let html = '';
                items.forEach(p => {
                    let b64 = IMAGENES[p.c];
                    let imgTag = b64 ? `<img src="data:image/png;base64,${b64}" class="producto-img" loading="lazy">` : `<div class="producto-img d-flex align-items-center justify-content-center text-muted border-bottom"><small style="font-size:0.7rem;">Sin foto</small></div>`;
                    let stockClass = p.s <= 5 ? 'stock-rojo' : (p.s <= 20 ? 'stock-amarillo' : 'stock-verde');
                    
                    // CARTEL REMARCADO 30% OFF EN LA IMAGEN
                    let badgeLiq = p.h === '🔥 LIQUIDACIÓN' ? `<span class='position-absolute top-0 end-0 m-2 badge bg-danger text-white fw-bold shadow' style='font-size:0.8rem; padding:5px 9px; border-radius:8px; z-index:11; letter-spacing:0.5px;'>💥 30% OFF</span>` : '';
                    
                    let preciosHtml = '';
                    for (const [tarifa, precio] of Object.entries(p.p)) {
                        if(!modoSeguridadActivo && tarifa !== 'SALGS') continue;
                        
                        if (p.h === '🔥 LIQUIDACIÓN') {
                            // Muestra el Antes (Tachado) y el Ahora en Rojo Liquidación
                            preciosHtml += `<div class='col-12 p-1'><div class='price-box border-danger' style='background-color:#FFF5F5;'><span class='text-muted d-block fw-bold' style='font-size:0.6rem; line-height:1;'>${tarifa}</span><span class='text-muted text-decoration-line-through d-block small' style='font-size:0.65rem;'>Antes: ${precio}</span><strong class='text-danger fw-black' style='font-size:0.85rem;'>🔥 Oferta: ${formatLiquidation(precio)}</strong></div></div>`;
                        } else {
                            // Tarjeta Normal
                            preciosHtml += `<div class='col-12 col-md-6 p-1'><div class='price-box'><span class='text-muted d-block fw-bold' style='font-size:0.6rem; line-height:1;'>${tarifa}</span><strong class='text-success fw-bold' style='font-size:0.75rem;'>${precio}</strong></div></div>`;
                        }
                    }
                    if(preciosHtml === '') {
                        preciosHtml = `<div class='col-12'><div class='price-box text-muted small fw-semibold py-1'>Consulte</div></div>`;
                    }
                    
                    html += `<div class='col tarjeta-contenedor'>
                        <div class='card card-producto shadow-sm d-flex flex-column justify-content-between h-100'>
                            <div class='position-relative' style='overflow:hidden;'>
                                ${badgeLiq}
                                ${imgTag}
                                <span class='position-absolute top-0 start-0 m-1 badge bg-dark font-monospace' style='font-size:0.7rem; padding:3px 6px;'>${p.c}</span>
                                <span class='position-absolute bottom-0 end-0 m-1 badge ${stockClass} fw-bold' style='font-size:0.75rem; padding:4px 7px;'>Stock: ${p.s}</span>
                            </div>
                            <div class='card-body d-flex flex-column justify-content-between p-2 bg-white' style='flex-grow:1;'>
                                <div class='mb-1'>
                                    <h6 class='fw-bold text-dark text-uppercase mb-0' style='font-size:0.78rem; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden; height:34px; line-height:1.1;'>${p.n}</h6>
                                    <small class='text-muted d-block font-weight-bold' style='font-size:0.68rem; overflow:hidden; white-space:nowrap; text-overflow:ellipsis;'>${p.m}</small>
                                </div>
                                <div class='row g-0 pt-1 border-top'>${preciosHtml}</div>
                            </div>
                        </div>
                    </div>`;
                });
                document.getElementById('grilla-productos').insertAdjacentHTML('beforeend', html); 
                paginaActual++;
            }

            window.addEventListener('scroll', () => {
                if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight - 900) {
                    if (paginaActual * ITEMS_POR_PAGINA < productosFiltrados.length) renderizarPagina();
                }
            });

            document.getElementById('buscadorWeb').addEventListener('input', function() {
                clearTimeout(debounceTimer); let query = this.value;
                debounceTimer = setTimeout(() => {
                    stateSearch = query; 
                    if (query !== '') { 
                        stateCat = 'Todo'; 
                        document.querySelectorAll('.btn-filtro').forEach(b => b.classList.remove('active')); 
                        document.querySelectorAll(`.btn-filtro[data-filtro="Todo"]`).forEach(b => b.add('active')); 
                    }
                    aplicarFiltros();
                }, 250);
            });

            document.addEventListener('click', function(e) {
                let filtroBtn = e.target.closest('.btn-filtro');
                if(filtroBtn) {
                    let val = filtroBtn.getAttribute('data-filtro');
                    document.querySelectorAll('.btn-filtro').forEach(b => b.classList.remove('active'));
                    document.querySelectorAll(`.btn-filtro[data-filtro="${val}"]`).forEach(b => b.classList.add('active'));
                    stateCat = val;
                    let buscador = document.getElementById('buscadorWeb');
                    if(buscador.value !== '') { buscador.value = ''; stateSearch = ''; }
                    aplicarFiltros();
                    
                    let canvasEl = document.getElementById('sidebarOffcanvas');
                    let instance = bootstrap.Offcanvas.getInstance(canvasEl);
                    if(instance) instance.hide();
                    window.scrollTo({top:0});
                }

                let tarifaBtn = e.target.closest('.btn-tarifa');
                if(tarifaBtn) {
                    let val = tarifaBtn.getAttribute('data-tarifa');
                    document.querySelectorAll('.btn-tarifa').forEach(b => b.classList.remove('active'));
                    document.querySelectorAll(`.btn-tarifa[data-tarifa="${val}"]`).forEach(b => b.classList.add('active'));
                    stateTarifa = val;
                    aplicarFiltros();
                }
            });

            function descargarPDFNativo() {
                let checkboxes = document.querySelectorAll('.check-tarifa-pdf:checked');
                let tarifasSeleccionadas = Array.from(checkboxes).map(cb => cb.value);
                if (tarifasSeleccionadas.length === 0) { alert('Por favor, tildá al menos 1 Tarifa.'); return; }
                
                let btnPdf = document.getElementById('btnGenerarPDF'); let originalText = btnPdf.innerHTML;
                btnPdf.innerHTML = '⏳ Procesando Archivo...'; btnPdf.disabled = true;

                setTimeout(async () => {
                    try {
                        const { jsPDF } = window.jspdf; const doc = new jsPDF();
                        let mostrarStock = document.getElementById('chkMostrarStock').checked;
                        let logoBase64 = '##LOGO_HTML##';
                        let textX = 14;
                        if (logoBase64.length > 100) {
                            let imgProps = doc.getImageProperties(logoBase64); let imgRatio = imgProps.height / imgProps.width;
                            let targetWidth = 45; let targetHeight = targetWidth * imgRatio;
                            if (targetHeight > 18) { targetHeight = 18; targetWidth = targetHeight / imgRatio; }
                            doc.addImage(logoBase64, 'PNG', 14, 10, targetWidth, targetHeight); textX = 14 + targetWidth + 5;
                        }
                        doc.setFontSize(16); doc.setTextColor(8, 18, 38); doc.text("CAMPING 44", textX, 16);
                        doc.setFontSize(10); doc.setTextColor(100, 100, 100); doc.text("Cotización de Salón", textX, 22);

                        let columnas = ["Img", "Código", "Descripción"];
                        if (mostrarStock) columnas.push("Stock");
                        tarifasSeleccionadas.forEach(t => columnas.push(t));

                        let filas = []; let urlsImagenes = [];
                        productosFiltrados.forEach(p => {
                            let preciosFila = []; let tienePrecio = false;
                            tarifasSeleccionadas.forEach(t => { 
                                if (p.p[t]) { 
                                    if (p.h === '🔥 LIQUIDACIÓN') {
                                        preciosFila.push(formatLiquidation(p.p[t]) + " (30% OFF)"); 
                                    } else {
                                        preciosFila.push(p.p[t]); 
                                    }
                                    tienePrecio = true; 
                                } else { 
                                    preciosFila.push('-'); 
                                    } 
                            });
                            if (!tienePrecio) return;
                            
                            let nombreFinal = p.h === '🔥 LIQUIDACIÓN' ? "[LIQ] " + p.n : p.n;
                            let row = ["", p.c, nombreFinal + "\\nMarca: " + p.m];
                            
                            if (mostrarStock) row.push(p.s.toString());
                            preciosFila.forEach(precio => row.push(precio));
                            filas.push(row); 
                            urlsImagenes.push(p.c || "");
                        });

                        doc.autoTable({
                            head: [columnas], body: filas, startY: 35, rowPageBreak: 'avoid',
                            styles: { fontSize: 8, valign: 'middle' },
                            headStyles: { fillColor: [8, 18, 38], textColor: 255 },
                            columnStyles: { 0: { cellWidth: 20, halign: 'center' }, 1: { cellWidth: 25 } },
                            bodyStyles: { minCellHeight: 20 },
                            didDrawCell: function(data) {
                                if (data.column.index === 0 && data.cell.section === 'body') {
                                    let b64Str = IMAGENES[data.row.index];
                                    if (b64Str) {
                                        try { doc.addImage("data:image/png;base64," + b64Str, 'PNG', data.cell.x + 2, data.cell.y + 2, 16, 16); } catch(e) {}
                                    }
                                }
                            }
                        });
                        doc.save("Cotizacion_Salon_Camping44.pdf");
                        btnPdf.innerHTML = originalText; btnPdf.disabled = false;
                    } catch (err) {
                        alert("Error al armar el PDF."); btnPdf.innerHTML = originalText; btnPdf.disabled = false;
                    }
                }, 100);
            }

            aplicarFiltros();
        </script></body></html>"""

        html = html.replace('##LOGO_HTML##', logo_html)
        html = html.replace('##JSON_DATA##', json_str)
        html = html.replace('##JSON_IMAGES##', json_images_str)

        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)
            
        print(f"¡Catálogo de Minoristas/Salón con Liquidación y precios 30% OFF generado con éxito!")

    except Exception as e:
        print(f"Error general: {e}")

if __name__ == "__main__":
    main()
