from fastapi.testclient import TestClient

from main import app

client = TestClient(app)



def test_post_noun1():
        role = 'patient'
        text = 'noun2'
        image = 'images/noun2.png'
        response = client.post(f"/post/noun?role={role}&noun={text}&path={image}")
        result = response.json()
        assert response.status_code == 200
        assert result['status'] == 'failure'
        
def test_post_noun2():
        role = 'doctor'
        text = 'noun1'
        image = 'images/noun1.png'
        response = client.post(f"/post/noun?role={role}&noun={text}&path={image}")
        result = response.json()
        assert response.status_code == 200
        assert result['status'] == 'success'
        assert result['noun'] == {'text': text, 'image': image}

def test_post_obAction1():
        role = 'patient'
        text = 'obAction2'
        image = 'images/obAction2.png'
        response = client.post(f"/post/obAction?role={role}&obAction={text}&path={image}")
        result = response.json()
        assert response.status_code == 200
        assert result['status'] == 'failure'
        
def test_post_obAction2():
        role = 'doctor'
        text = 'obAction1'
        image = 'images/obAction1.png'
        response = client.post(f"/post/obAction?role={role}&obAction={text}&path={image}")
        result = response.json()
        assert response.status_code == 200
        assert result['status'] == 'success'
        assert result['obAction'] == {'text': text, 'image': image}

def test_post_subAction1():
        role = 'patient'
        text = 'subAction2'
        image = 'images/subAction2.png'
        response = client.post(f"/post/subAction?role={role}&subAction={text}&path={image}")
        result = response.json()
        assert response.status_code == 200
        assert result['status'] == 'failure'

def test_post_subAction2():
        role = 'doctor'
        text = 'subAction1'
        image = 'images/subAction1.png'
        response = client.post(f"/post/subAction?role={role}&subAction={text}&path={image}")
        result = response.json()
        assert response.status_code == 200
        assert result['status'] == 'success'
        assert result['subAction'] == {'text': text, 'image': image}
        
def test_post_adjective1():
        role = 'patient'
        text = 'adjective2'
        image = 'images/adjective2.png'
        response = client.post(f"/post/adjective?role={role}&adjective={text}&path={image}")
        result = response.json()
        assert response.status_code == 200
        assert result['status'] == 'failure'

def test_post_adjective2():
        role = 'doctor'
        text = 'adjective1'
        image = 'images/adjective1.png'
        response = client.post(f"/post/adjective?role={role}&adjective={text}&path={image}")
        result = response.json()
        assert response.status_code == 200
        assert result['status'] == 'success'
        assert result['adjective'] == {'text': text, 'image': image}

        
def test_post_owner1():
        role = 'patient'
        owner = 'owner2'
        date = '2005-02-15'
        desease = 'desease2'
        response = client.post(f"/post/owner?role={role}&owner={owner}&date={date}&desease={desease}")
        result = response.json()
        assert response.status_code == 200
        assert result['status'] == 'failure'

def test_post_owner2():
        role = 'doctor'
        owner = 'owner1'
        date = '2005-02-15'
        desease = 'desease1'
        response = client.post(f"/post/owner?role={role}&owner={owner}&date={date}&desease={desease}")
        result = response.json()
        assert response.status_code == 200
        assert result['status'] == 'success'
        assert result['owner']['name'] == owner
        assert result['owner']['desease'] == desease

def test_post_noun2adjective1():
        role = 'patient'
        noun = 'noun1'
        nounImage = 'images/noun1.png'
        adjective = 'adjective1'
        adjectiveImage = 'images/adjective1.png'
        response = client.post(f"/post/noun2adjective?role={role}&noun={noun}&adjective={adjective}")
        result = response.json()
        assert response.status_code == 200
        assert result['status'] == 'failure'

def test_post_noun2adjective2():
        role = 'doctor'
        noun = 'noun1'
        nounImage = 'images/noun1.png'
        adjective = 'adjective1'
        adjectiveImage = 'images/adjective1.png'
        response = client.post(f"/post/noun2adjective?role={role}&noun={noun}&adjective={adjective}")
        result = response.json()
        assert response.status_code == 200
        assert result['status'] == 'success'
        assert result['nodes'] == [{'text': noun, 'image': nounImage}, {'text': adjective, 'image': adjectiveImage}]

def test_post_noun2subAction1():
        role = 'patient'
        noun = 'noun1'
        nounImage = 'images/noun1.png'
        subAction = 'subAction1'
        subActionImage = 'images/subAction1.png'
        response = client.post(f"/post/noun2subAction?role={role}&noun={noun}&subAction={subAction}")
        result = response.json()
        assert response.status_code == 200
        assert result['status'] == 'failure'

def test_post_noun2subAction2():
        role = 'doctor'
        noun = 'noun1'
        nounImage = 'images/noun1.png'
        subAction = 'subAction1'
        subActionImage = 'images/subAction1.png'
        response = client.post(f"/post/noun2subAction?role={role}&noun={noun}&subAction={subAction}")
        result = response.json()
        assert response.status_code == 200
        assert result['status'] == 'success'
        assert result['nodes'] == [{'text': noun, 'image': nounImage}, {'text': subAction, 'image': subActionImage}]

def test_post_noun2obAction1():
        role = 'patient'
        noun = 'noun1'
        nounImage = 'images/noun1.png'
        obAction = 'obAction1'
        obActionImage = 'images/obAction1.png'
        response = client.post(f"/post/noun2obAction?role={role}&noun={noun}&obAction={obAction}")
        result = response.json()
        assert response.status_code == 200
        assert result['status'] == 'failure'

def test_post_noun2obAction2():
        role = 'doctor'
        noun = 'noun1'
        nounImage = 'images/noun1.png'
        obAction = 'obAction1'
        obActionImage = 'images/obAction1.png'
        response = client.post(f"/post/noun2obAction?role={role}&noun={noun}&obAction={obAction}")
        result = response.json()
        assert response.status_code == 200
        assert result['status'] == 'success'
        assert result['nodes'] == [{'text': noun, 'image': nounImage}, {'text': obAction, 'image': obActionImage}]

def test_post_subAction2adjective1():
        role = 'patient'
        subAction = 'subAction1'
        subActionImage = 'images/subAction1.png'
        adjective = 'adjective1'
        adjectiveImage = 'images/adjective1.png'
        response = client.post(f"/post/subAction2adjective?role={role}&subAction={subAction}&adjective={adjective}")
        result = response.json()
        assert response.status_code == 200
        assert result['status'] == 'failure'

def test_post_subAction2adjective2():
        role = 'doctor'
        subAction = 'subAction1'
        subActionImage = 'images/subAction1.png'
        adjective = 'adjective1'
        adjectiveImage = 'images/adjective1.png'
        response = client.post(f"/post/subAction2adjective?role={role}&subAction={subAction}&adjective={adjective}")
        result = response.json()
        assert response.status_code == 200
        assert result['status'] == 'success'
        assert result['nodes'] == [{'text': subAction, 'image': subActionImage}, {'text': adjective, 'image': adjectiveImage}]

def test_post_obAction2adjective1():
        role = 'patient'
        obAction = 'obAction1'
        obActionImage = 'images/obAction1.png'
        adjective = 'adjective1'
        adjectiveImage = 'images/adjective1.png'
        response = client.post(f"/post/obAction2adjective?role={role}&obAction={obAction}&adjective={adjective}")
        result = response.json()
        assert response.status_code == 200
        assert result['status'] == 'failure'

def test_post_obAction2adjective2():
        role = 'doctor'
        obAction = 'obAction1'
        obActionImage = 'images/obAction1.png'
        adjective = 'adjective1'
        adjectiveImage = 'images/adjective1.png'
        response = client.post(f"/post/obAction2adjective?role={role}&obAction={obAction}&adjective={adjective}")
        result = response.json()
        assert response.status_code == 200
        assert result['status'] == 'success'
        assert result['nodes'] == [{'text': obAction, 'image': obActionImage}, {'text': adjective, 'image': adjectiveImage}]

def test_post_owner2noun1():
        role = 'patient'
        noun = 'noun1'
        nounImage = 'images/noun1.png'
        owner = 'owner1'
        date = '2005-02-15'
        desease = 'desease1'
        response = client.post(f"/post/owner2noun?role={role}&owner={owner}&noun={noun}&path={nounImage}")
        result = response.json()
        assert response.status_code == 200
        assert result['status'] == 'failure'

def test_post_owner2noun2():
        role = 'doctor'
        noun = 'noun1'
        nounImage = 'images/noun1.png'
        owner = 'owner1'
        date = '2005-02-15'
        desease = 'desease1'
        response = client.post(f"/post/owner2noun?role={role}&owner={owner}&noun={noun}&path={nounImage}")
        result = response.json()
        assert response.status_code == 200
        assert result['status'] == 'success'
        assert result['nodes'][0]['name'] == owner
        assert result['nodes'][1] == {'text': noun, 'image': nounImage}

def test_post_owner2obAction1():
        role = 'patient'
        obAction = 'obAction1'
        obActionImage = 'images/obAction1.png'
        owner = 'owner1'
        date = '2005-02-15'
        desease = 'desease1'
        response = client.post(f"/post/owner2obAction?role={role}&owner={owner}&obAction={obAction}&path={obActionImage}")
        result = response.json()
        assert response.status_code == 200
        assert result['status'] == 'failure'

def test_post_owner2obAction2():
        role = 'doctor'
        obAction = 'obAction1'
        obActionImage = 'images/obAction1.png'
        owner = 'owner1'
        date = '2005-02-15'
        desease = 'desease1'
        response = client.post(f"/post/owner2obAction?role={role}&owner={owner}&obAction={obAction}&path={obActionImage}")
        result = response.json()
        assert response.status_code == 200
        assert result['status'] == 'success'
        assert result['nodes'][0]['name'] == owner
        assert result['nodes'][1] == {'text': obAction, 'image': obActionImage}

def test_post_owner2subAction1():
        role = 'patient'
        subAction = 'subAction1'
        subActionImage = 'images/subAction1.png'
        owner = 'owner1'
        date = '2005-02-15'
        desease = 'desease1'
        response = client.post(f"/post/owner2subAction?role={role}&owner={owner}&subAction={subAction}&path={subActionImage}")
        result = response.json()
        assert response.status_code == 200
        assert result['status'] == 'failure'

def test_post_owner2subAction2():
        role = 'doctor'
        subAction = 'subAction1'
        subActionImage = 'images/subAction1.png'
        owner = 'owner1'
        date = '2005-02-15'
        desease = 'desease1'
        response = client.post(f"/post/owner2subAction?role={role}&owner={owner}&subAction={subAction}&path={subActionImage}")
        result = response.json()
        assert response.status_code == 200
        assert result['status'] == 'success'
        assert result['nodes'][0]['name'] == owner
        assert result['nodes'][1] == {'text': subAction, 'image': subActionImage}

def test_post_owner2adjective1():
        role = 'patient'
        adjective = 'adjective1'
        adjectiveImage = 'images/adjective1.png'
        owner = 'owner1'
        date = '2005-02-15'
        desease = 'desease1'
        response = client.post(f"/post/owner2adjective?role={role}&owner={owner}&adjective={adjective}&path={adjectiveImage}")
        result = response.json()
        assert response.status_code == 200
        assert result['status'] == 'failure'

def test_post_owner2adjective2():
        role = 'doctor'
        adjective = 'adjective1'
        adjectiveImage = 'images/adjective1.png'
        owner = 'owner1'
        date = '2005-02-15'
        desease = 'desease1'
        response = client.post(f"/post/owner2adjective?role={role}&owner={owner}&adjective={adjective}&path={adjectiveImage}")
        result = response.json()
        assert response.status_code == 200
        assert result['status'] == 'success'
        assert result['nodes'][0]['name'] == owner
        assert result['nodes'][1] == {'text': adjective, 'image': adjectiveImage}

# READ

def test_get_all1():
    role = 'patient'
    response = client.get(f"/get/all?role={role}")
    result = response.json()
    assert response.status_code == 200
    assert result['status'] == 'success'
    assert result['results'] == 141

def test_get_all2():
    role = 'doctor'
    response = client.get(f"/get/all?role={role}")
    result = response.json()
    assert response.status_code == 200
    assert result['status'] == 'success'
    assert result['results'] == 141

def test_get_allByOwner1():
    role = 'patient'
    owner = 'Lorem ipsum'
    response = client.get(f"/get/allByOwner?role={role}&owner={owner}")
    result = response.json()
    assert response.status_code == 200
    assert result['status'] == 'success'
    assert result['results'] == 135

def test_get_allByOwner2():
    role = 'doctor'
    owner = 'Lorem ipsum'
    response = client.get(f"/get/allByOwner?role={role}&owner={owner}")
    result = response.json()
    assert response.status_code == 200
    assert result['status'] == 'success'
    assert result['results'] == 135

def test_get_all_nouns1():
    role = 'patient'
    owner = 'Lorem ipsum'
    response = client.get(f"/get/all_nouns?role={role}&owner={owner}")
    result = response.json()
    assert response.status_code == 200
    assert result['status'] == 'success'
    assert result['results'] == 49

def test_get_all_nouns2():
    role = 'doctor'
    owner = 'Lorem ipsum'
    response = client.get(f"/get/all_nouns?role={role}&owner={owner}")
    result = response.json()
    assert response.status_code == 200
    assert result['status'] == 'success'
    assert result['results'] == 49

def test_get_subActionsByNoun1():
    role = 'patient'
    owner = 'Lorem ipsum'
    noun = 'lorem'
    response = client.get(f"/get/subActionsByNoun?role={role}&owner={owner}&noun={noun}")
    result = response.json()
    assert response.status_code == 200
    assert result['status'] == 'success'
    assert result['results'] == 1

def test_get_subActionsByNoun2():
    role = 'doctor'
    owner = 'Lorem ipsum'
    noun = 'lorem'
    response = client.get(f"/get/subActionsByNoun?role={role}&owner={owner}&noun={noun}")
    result = response.json()
    assert response.status_code == 200
    assert result['status'] == 'success'
    assert result['results'] == 1

def test_get_obActionsByNoun1():
    role = 'patient'
    owner = 'Lorem ipsum'
    noun = 'lorem'
    response = client.get(f"/get/obActionsByNoun?role={role}&owner={owner}&noun={noun}")
    result = response.json()
    assert response.status_code == 200
    assert result['status'] == 'success'
    assert result['results'] == 3

def test_get_obActionsByNoun2():
    role = 'doctor'
    owner = 'Lorem ipsum'
    noun = 'lorem'
    response = client.get(f"/get/obActionsByNoun?role={role}&owner={owner}&noun={noun}")
    result = response.json()
    assert response.status_code == 200
    assert result['status'] == 'success'
    assert result['results'] == 3

def test_get_adjectiveByNoun1():
    role = 'patient'
    owner = 'Lorem ipsum'
    noun = 'lorem'
    response = client.get(f"/get/adjectiveByNoun?role={role}&owner={owner}&noun={noun}")
    result = response.json()
    assert response.status_code == 200
    assert result['status'] == 'success'
    assert result['results'] == 1

def test_get_adjectiveByNoun2():
    role = 'doctor'
    owner = 'Lorem ipsum'
    noun = 'lorem'
    response = client.get(f"/get/adjectiveByNoun?role={role}&owner={owner}&noun={noun}")
    result = response.json()
    assert response.status_code == 200
    assert result['status'] == 'success'
    assert result['results'] == 1

def test_get_adjectiveByObAction1():
    role = 'patient'
    owner = 'Lorem ipsum'
    obAction = 'lorem'
    response = client.get(f"/get/adjectiveByObAction?role={role}&owner={owner}&obAction={obAction}")
    result = response.json()
    assert response.status_code == 200
    assert result['status'] == 'success'
    assert result['results'] == 0

def test_get_adjectiveByObAction2():
    role = 'doctor'
    owner = 'Lorem ipsum'
    obAction = 'lorem'
    response = client.get(f"/get/adjectiveByObAction?role={role}&owner={owner}&obAction={obAction}")
    result = response.json()
    assert response.status_code == 200
    assert result['status'] == 'success'
    assert result['results'] == 0

def test_get_adjectiveBySubAction1():
    role = 'patient'
    owner = 'Lorem ipsum'
    subAction = 'lorem'
    response = client.get(f"/get/adjectiveBySubAction?role={role}&owner={owner}&subAction={subAction}")
    result = response.json()
    assert response.status_code == 200
    assert result['status'] == 'success'
    assert result['results'] == 0

def test_get_adjectiveBySubAction2():
    role = 'doctor'
    owner = 'Lorem ipsum'
    subAction = 'lorem'
    response = client.get(f"/get/adjectiveBySubAction?role={role}&owner={owner}&subAction={subAction}")
    result = response.json()
    assert response.status_code == 200
    assert result['status'] == 'success'
    assert result['results'] == 0

# UPDATE


def test_patch_noun1():
    role = 'patient'
    owner = 'owner1'
    noun = 'noun1'
    nounImage = 'images/noun1.png'
    new_nounImage = 'images/new_noun1.png'
    response = client.patch(f"/patch/noun?role={role}&owner={owner}&noun={noun}&path={nounImage}&new_path={new_nounImage}")
    result = response.json()
    assert response.status_code == 200
    assert result['status'] == 'failure'

def test_patch_noun2():
    role = 'doctor'
    owner = 'owner1'
    noun = 'noun1'
    nounImage = 'images/noun1.png'
    new_nounImage = 'images/new_noun1.png'
    response = client.patch(f"/patch/noun?role={role}&owner={owner}&noun={noun}&path={nounImage}&new_path={new_nounImage}")
    result = response.json()
    assert response.status_code == 200
    assert result['status'] == 'success'
    assert result['nodes'][0]['name'] == 'owner1'
    assert result['nodes'][1] == {'text': noun, 'image': new_nounImage}

def test_patch_obAction1():
    role = 'patient'
    owner = 'owner1'
    obAction = 'obAction1'
    obActionImage = 'images/obAction1.png'
    new_obActionImage = 'images/new_obAction1.png'
    response = client.patch(f"/patch/obAction?role={role}&owner={owner}&obAction={obAction}&path={obActionImage}&new_path={new_obActionImage}")
    result = response.json()
    assert response.status_code == 200
    assert result['status'] == 'failure'

def test_patch_obAction2():
    role = 'doctor'
    owner = 'owner1'
    obAction = 'obAction1'
    obActionImage = 'images/obAction1.png'
    new_obActionImage = 'images/new_obAction1.png'
    response = client.patch(f"/patch/obAction?role={role}&owner={owner}&obAction={obAction}&path={obActionImage}&new_path={new_obActionImage}")
    result = response.json()
    assert response.status_code == 200
    assert result['status'] == 'success'
    assert result['nodes'][0]['name'] == 'owner1'
    assert result['nodes'][1] == {'text': obAction, 'image': new_obActionImage}

def test_patch_subAction1():
    role = 'patient'
    owner = 'owner1'
    subAction = 'subAction1'
    subActionImage = 'images/subAction1.png'
    new_subActionImage = 'images/new_subAction1.png'
    response = client.patch(f"/patch/subAction?role={role}&owner={owner}&subAction={subAction}&path={subActionImage}&new_path={new_subActionImage}")
    result = response.json()
    assert response.status_code == 200
    assert result['status'] == 'failure'

def test_patch_subAction2():
    role = 'doctor'
    owner = 'owner1'
    subAction = 'subAction1'
    subActionImage = 'images/subAction1.png'
    new_subActionImage = 'images/new_subAction1.png'
    response = client.patch(f"/patch/subAction?role={role}&owner={owner}&subAction={subAction}&path={subActionImage}&new_path={new_subActionImage}")
    result = response.json()
    assert response.status_code == 200
    assert result['status'] == 'success'
    assert result['nodes'][0]['name'] == 'owner1'
    assert result['nodes'][1] == {'text': subAction, 'image': new_subActionImage}

def test_patch_adjective1():
    role = 'patient'
    owner = 'owner1'
    adjective = 'adjective1'
    adjectiveImage = 'images/adjective1.png'
    new_adjectiveImage = 'images/new_adjective1.png'
    response = client.patch(f"/patch/adjective?role={role}&owner={owner}&adjective={adjective}&path={adjectiveImage}&new_path={new_adjectiveImage}")
    result = response.json()
    assert response.status_code == 200
    assert result['status'] == 'failure'

def test_patch_adjective2():
    role = 'doctor'
    owner = 'owner1'
    adjective = 'adjective1'
    adjectiveImage = 'images/adjective1.png'
    new_adjectiveImage = 'images/new_adjective1.png'
    response = client.patch(f"/patch/adjective?role={role}&owner={owner}&adjective={adjective}&path={adjectiveImage}&new_path={new_adjectiveImage}")
    result = response.json()
    assert response.status_code == 200
    assert result['status'] == 'success'
    assert result['nodes'][0]['name'] == 'owner1'
    assert result['nodes'][1] == {'text': adjective, 'image': new_adjectiveImage}

def test_patch_owner1():
    role = 'patient'
    owner = 'owner1'
    date = '2005-02-15'
    desease = 'desease1'
    new_desease = 'new_desease1'
    response = client.patch(f"/patch/owner?role={role}&owner={owner}&date={date}&desease={desease}&new_desease={new_desease}")
    result = response.json()
    assert response.status_code == 200
    assert result['status'] == 'failure'

def test_patch_owner2():
    role = 'doctor'
    owner = 'owner1'
    date = '2005-02-15'
    desease = 'desease1'
    new_desease = 'new_desease1'
    response = client.patch(f"/patch/owner?role={role}&owner={owner}&date={date}&desease={desease}&new_desease={new_desease}")
    result = response.json()
    assert response.status_code == 200
    assert result['status'] == 'success'
    assert result['nodes'][0]['name'] == 'owner1'
    assert result['nodes'][0]['desease'] == 'new_desease1'

# DELETE


def test_delete_noun1():
    role = 'patient'
    noun = 'noun1'
    nounImage = 'images/new_noun1.png'
    response = client.delete(f"/delete/noun?role={role}&noun={noun}&path={nounImage}")
    result = response.json()
    assert response.status_code == 200
    assert result['status'] == 'failure'

def test_delete_noun2():
    role = 'doctor'
    noun = 'noun1'
    nounImage = 'images/new_noun1.png'
    response = client.delete(f"/delete/noun?role={role}&noun={noun}&path={nounImage}")
    result = response.json()
    assert response.status_code == 200
    assert result['status'] == 'success'

def test_delete_obAction1():
    role = 'patient'
    obAction = 'obAction1'
    obActionImage = 'images/new_obAction1.png'
    response = client.delete(f"/delete/obAction?role={role}&obAction={obAction}&path={obActionImage}")
    result = response.json()
    assert response.status_code == 200
    assert result['status'] == 'failure'

def test_delete_obAction2():
    role = 'doctor'
    obAction = 'obAction1'
    obActionImage = 'images/new_obAction1.png'
    response = client.delete(f"/delete/obAction?role={role}&obAction={obAction}&path={obActionImage}")
    result = response.json()
    assert response.status_code == 200
    assert result['status'] == 'success'

def test_delete_subAction1():
    role = 'patient'
    subAction = 'subAction1'
    subActionImage = 'images/new_subAction1.png'
    response = client.delete(f"/delete/subAction?role={role}&subAction={subAction}&path={subActionImage}")
    result = response.json()
    assert response.status_code == 200
    assert result['status'] == 'failure'

def test_delete_subAction2():
    role = 'doctor'
    subAction = 'subAction1'
    subActionImage = 'images/new_subAction1.png'
    response = client.delete(f"/delete/subAction?role={role}&subAction={subAction}&path={subActionImage}")
    result = response.json()
    assert response.status_code == 200
    assert result['status'] == 'success'

def test_delete_adjective1():
    role = 'patient'
    adjective = 'adjective1'
    adjectiveImage = 'images/new_adjective1.png'
    response = client.delete(f"/delete/adjective?role={role}&adjective={adjective}&path={adjectiveImage}")
    result = response.json()
    assert response.status_code == 200
    assert result['status'] == 'failure'

def test_delete_adjective2():
    role = 'doctor'
    adjective = 'adjective1'
    adjectiveImage = 'images/new_adjective1.png'
    response = client.delete(f"/delete/adjective?role={role}&adjective={adjective}&path={adjectiveImage}")
    result = response.json()
    assert response.status_code == 200
    assert result['status'] == 'success'

def test_delete_owner1():
    role = 'patient'
    owner = 'owner1'
    date = '2005-02-15'
    desease = 'new_desease1'
    response = client.delete(f"/delete/owner?role={role}&owner={owner}&date={date}&desease={desease}")
    result = response.json()
    assert response.status_code == 200
    assert result['status'] == 'failure'

def test_delete_owner2():
    role = 'doctor'
    owner = 'owner1'
    date = '2005-02-15'
    desease = 'new_desease1'
    response = client.delete(f"/delete/owner?role={role}&owner={owner}&date={date}&desease={desease}")
    result = response.json()
    assert response.status_code == 200
    assert result['status'] == 'success'