import psycopg2
from pandas import DataFrame

def fetch (tag):
    conn = psycopg2.connect("dbname=derpibooru user=postgres")
    cur = conn.cursor()
    cur.execute("""
                SELECT public.images.id, public.images.created_at, public.image_taggings.tag_id, public.tags.name 
                FROM public.images 
                JOIN public.image_taggings ON public.images.id = public.image_taggings.image_id 
                JOIN public.tags ON public.image_taggings.tag_id = public.tags.id 
                WHERE public.tags.name = %s;
                """,
                [tag])
    result = DataFrame(cur.fetchall(), columns=['image_id', 'date', 'tag_id', 'tag_name'])
    cur.close()
    conn.close()
    return result
