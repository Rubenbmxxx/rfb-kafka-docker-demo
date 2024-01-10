select *
from pokedex.random_appears
limit 10

select count(*)
from pokedex.random_appears

select pokemon, count(*)
from pokedex.random_appears
group by pokemon
having count(*) > 1