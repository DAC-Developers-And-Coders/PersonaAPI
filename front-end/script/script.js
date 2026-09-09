const API_URL = 'http://localhost:8000/';

const createPersona = (personaName, personaOrigin, firstAppearance, personaClass, initialLevel, arcana_id, element_id) => {
    if (!personaName || !personaOrigin || !firstAppearance || !initialLevel || arcana_id === null || !element_id) {
        throw new Error('Todos os campos, exceto a classe, são obrigatórios para criar uma persona.');
    }

    if (typeof initialLevel !== 'number' || initialLevel < 1) {
        throw new Error('O nível inicial deve ser um número inteiro positivo.');
    }

    if (typeof arcana_id !== 'number' || arcana_id < 0) {
        throw new Error('O ID do Arcana deve ser um número inteiro (a partir de 0) positivo.');
    }

    if (typeof element_id !== 'number' || element_id < 1) {
        throw new Error('O ID do Elemento deve ser um número inteiro positivo.');
    }

    return {
        "nome": personaName,
        "origem": personaOrigin,
        "primeira_aparicao": firstAppearance,
        "classe": personaClass,
        "nivel_inicial": initialLevel,
        "arcana_id": arcana_id,
        "elemento_id": element_id
    }
}

const request = async (endpoint, requestOptions) => {
    try {
        const response = await fetch(`${API_URL}${endpoint}`, requestOptions);
        if (!response.ok) {
            const errorData = await response.json();

            throw new Error(`${errorData.detail}: ${response.status}`);
        }

        if ((response.status === 204 && requestOptions?.method !== 'OPTIONS') || requestOptions?.method === 'HEAD') {
            return response.headers.get('mensagem');
        } else if (requestOptions?.method === 'OPTIONS') {
            return response.headers.get('Allow');
        }

        return await response.json();
    } catch (error) {
        console.error(error);
    }
};

const getAllPersonas = async () => {
    return await request('personas');
}

const getSpecificPersona = async (id) => {
    return await request(`personas/${id}`);
}

const getAllElements = async () => {
    return await request('elementos');
}

const getSpecificElement = async (id) => {
    return await request(`elementos/${id}`);
}

const getAllArcanas = async () => {
    return await request('arcanas');
}

const getSpecificArcana = async (id) => {
    return await request(`arcanas/${id}`);
}

const addPersona = async (persona) => {
    const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(persona)
    }

    return await request('personas', requestOptions);
}

const updatePersona = async (id, persona) => {
    const requestOptions = {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(persona)
    }

    return await request(`personas/${id}`, requestOptions);
}

const updatePersonaAttribute = async (id, attribute, value) => {
    const requestOptions = {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(value)
    }

    return await request(`personas/${id}/${attribute}`, requestOptions);
}

const deletePersona = async (id) => {
    const requestOptions = {
        method: 'DELETE'
    };

    return await request(`personas/${id}`, requestOptions);
}

const verifyPersona = async () => {
    const requestOptions = {
        method: 'HEAD'
    };

    return await request(`personas`, requestOptions);
}

const verifySpecificPersona = async (id) => {
    const requestOptions = {
        method: 'HEAD'
    };

    return await request(`personas/${id}`, requestOptions);
}

const verifyElements = async () => {
    const requestOptions = {
        method: 'HEAD'
    };

    return await request(`elementos`, requestOptions);
}

const verifySpecificElements = async (id) => {
    const requestOptions = {
        method: 'HEAD'
    };

    return await request(`elementos/${id}`, requestOptions);
}

const verifyArcanas = async () => {
    const requestOptions = {
        method: 'HEAD'
    };

    return await request(`arcanas`, requestOptions);
}

const verifySpecificArcana = async (id) => {
    const requestOptions = {
        method: 'HEAD'
    };

    return await request(`arcanas/${id}`, requestOptions);
}

const verifyPersonaOptions = async () => {
    const requestOptions = {
        method: 'OPTIONS'
    };

    return await request(`personas`, requestOptions);
}

const verifyElementsOptions = async () => {
    const requestOptions = {
        method: 'OPTIONS'
    };

    return await request(`elementos`, requestOptions);
}

const verifyArcanasOptions = async () => {
    const requestOptions = {
        method: 'OPTIONS'
    };

    return await request(`arcanas`, requestOptions);
}

const main = async () => {
    const personas = await getAllPersonas();
    const persona = await getSpecificPersona(9);
    //const newPersona = createPersona("Shiki-Ouji", "Mitologia Japonesa", "Shin Megami Tensei: Devil Summoner", null, 18, 0, 7);
    //const addedPersona = await addPersona(newPersona);
    //const deletePersonaResponse = await deletePersona(23);
    //const updatePersonaData = await updatePersona(20, newPersona)
    //const updatePersonaAttributeResponse = await updatePersonaAttribute(20, "origem", "Mitologia Chinesa");
    const verifySpecificPersonaResponse = await verifySpecificPersona(20);
    const verifyPersonaResponse = await verifyPersona();
    const verifyPersonaOptionsResponse = await verifyPersonaOptions();

    const elements = await getAllElements();
    const element = await getSpecificElement(9);
    const verifySpecificElementResponse = await verifySpecificElements(3);
    const verifyElementsResponse = await verifyElements();
    const verifyElementsOptionsResponse = await verifyElementsOptions();

    const arcanas = await getAllArcanas();
    const arcana = await getSpecificArcana(0);
    const verifySpecificArcanaResponse = await verifySpecificArcana(3);
    const verifyArcanasResponse = await verifyArcanas();
    const verifyArcanasOptionsResponse = await verifyArcanasOptions();

    console.log(personas);
    console.log(persona);
    console.log(verifySpecificPersonaResponse);
    console.log(verifyPersonaResponse);
    console.log(verifyPersonaOptionsResponse);

    console.log(elements);
    console.log(element);
    console.log(verifySpecificElementResponse);
    console.log(verifyElementsResponse);
    console.log(verifyElementsOptionsResponse);

    console.log(arcanas);
    console.log(arcana);
    console.log(verifySpecificArcanaResponse);
    console.log(verifyArcanasResponse);
    console.log(verifyArcanasOptionsResponse);
    
    //console.log(addedPersona);
    //console.log(deletePersonaResponse);
    //console.log(updatePersonaData);
    //console.log(updatePersonaAttributeResponse);
};

main();