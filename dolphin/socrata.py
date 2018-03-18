import pandas as pd

catalog = \
    {'pr-record-de-votacion-de-senado': \
        {'title': 'Record de Votación de Senado',
        'json': 'https://data.pr.gov/resource/byvm-x9d7.json',
        'link': 'https://data.pr.gov/en/Abierto/Record-de-Votaci-n-de-Senado/fu3e-fj3e'},

    'pr-escuelas-publicas': \
        {'title': 'Directorio Comprensivo de Escuelas Públicas, Puerto Rico 2017',
        'json': 'https://data.pr.gov/resource/ceib-pqg3.json',
        'link': 'https://data.pr.gov/en/Educaci-n/Directorio-Comprensivo-de-Escuelas-P-blicas-Puerto/gb92-58gc'},

    'pr-mapa-de-donaciones-recibidas': \
       {'title': 'Mapa de donaciones recibidas por código postal',
       'json': 'https://data.oce.gov.pr/resource/gd5x-wf9i.json',
       'link': 'https://data.oce.gov.pr/Donaciones/Mapa-de-donaciones-recibidas-por-c-digo-postal/gd5x-wf9i'},

    'pr-beneficios-de-pan-y-tanf': \
       {'title': 'Estadisticas de Beneficios de PAN y TANF',
       'json': 'https://data.pr.gov/resource/b9xp-ve5k.json',
       'link': 'https://data.pr.gov/en/Familia-y-Servicio-Social/Estadisticas-de-Beneficios-de-PAN-y-TANF/rd77-7s4b'},

    'pr-mapa-del-crimen': \
       {'title': 'Mapa del Crimen',
       'json': 'https://data.pr.gov/resource/bkiv-k4gu.json',
       'link': 'https://data.pr.gov/en/Seguridad-P-blica/Mapa-del-Crimen-Crime-Map/bkiv-k4gu'}
    }

def retrieve_raw_data(data_tag):
    '''Uses Socrata API to generate and return raw data'''
    return pd.read_json(catalog[data_tag]['json'])
