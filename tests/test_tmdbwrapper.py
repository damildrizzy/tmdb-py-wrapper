from tmdbwrapper import Tv
from pytest import fixture
import vcr



@fixture
def tv_keys():
    return ['id', 'origin_country', 'poster_path', 'name',
              'overview', 'popularity', 'backdrop_path',
              'first_air_date', 'vote_count', 'vote_average']

@vcr.use_cassette('tests/vcr_cassettes/tv_info.yml')
def test_tv_info(tv_keys):
    tv_instance = Tv(1396)
    response = tv_instance.info()

    assert isinstance(response, dict)
    assert response['id']==1396, "The ID should be included in the response"
    assert set(tv_keys).issubset(response.keys()), "all keys should be in the response"


@vcr.use_cassette('tests/vcr_cassettes/tv_popular.yml, filter_query_parameters=['api_key']')
def test_tv_popular():
    response = Tv.popular()

    assert isinstance(response, dict)
    assert isinstance(response['results'], list)
    assert isinstance(response['results'][0], dict)
    #assert set(tv_keys).issubset(response['results'][0].keys())
