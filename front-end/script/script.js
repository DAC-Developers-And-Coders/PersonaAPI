const API_URL = 'http://localhost:8000/';

const createPersona = (personaName, personaOrigin, firstAppearance, personaClass, initialLevel, arcana_id, element_id) => {
    if (!personaName || !personaOrigin || !firstAppearance || !initialLevel || arcana_id === null || arcana_id === '' || !element_id) {
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
            if (requestOptions?.method === 'HEAD') {
                const message = response.headers.get('mensagem');
                throw new Error(`${message}: ${response.status}`);
            }

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
        throw error;
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

const showResult = (element, message) => {
    element.textContent = message;
}

const personaResult = document.querySelector('.result-persona');
const elementsResult = document.querySelector('.result-elemento');
const arcanasResult = document.querySelector('.result-arcano');

const createPersonaForm = document.querySelector('#create-persona-form');
const searchPersonaForm = document.querySelector('#search-persona-form');
const deletePersonaForm = document.querySelector('#delete-persona-form');
const optionsButton = document.querySelector('#options');

const elementsForm = document.querySelector('#elements-form');
const arcanaForm = document.querySelector('#arcana-form');

createPersonaForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const action = event.submitter.getAttribute('data-action');
    const formData = new FormData(createPersonaForm);

    try {
        const personaName = formData.get('name').trim();
        const personaOrigin = formData.get('origem').trim();
        const firstAppearance = formData.get('primeira_aparicao').trim();
        const personaClass = formData.get('classe').trim();

        const initialLevel = Number(formData.get('nivel_inicial').trim());
        const arcana_id = parseInt(formData.get('arcana_id').trim());
        const element_id = parseInt(formData.get('elemento_id').trim());

        if (action === 'create'){
            const newPersona = createPersona(personaName, personaOrigin, firstAppearance, personaClass, initialLevel, arcana_id, element_id);

            const result = await addPersona(newPersona);
            showResult(personaResult, `Persona ${result.nome} adicionada com sucesso! ID: ${result.id}`);
        } else if (action === 'update') {
            const personaId = parseInt(formData.get('id').trim());

            const updatedPersona = createPersona(personaName, personaOrigin, firstAppearance, personaClass, initialLevel, arcana_id, element_id);

            const result = await updatePersona(personaId, updatedPersona);
            showResult(personaResult, `Persona ${result.nome} atualizada com sucesso! ID: ${result.id}`);
        } else if (action === 'update-patch') {
            const personaId = parseInt(formData.get('id').trim());

            const fields = {
                nome: formData.get('name').trim(),
                origem: formData.get('origem').trim(),
                primeira_aparicao: formData.get('primeira_aparicao').trim(),
                classe: formData.get('classe').trim(),
                nivel_inicial: formData.get('nivel_inicial'),
                arcana_id: formData.get('arcana_id'),
                elemento_id: formData.get('elemento_id')
            };

            for (const [attribute, value] of Object.entries(fields)) {
                if (value !== '') {
                    let convertedValue = value;

                    if (attribute === 'nivel_inicial' ||
                        attribute === 'arcana_id' ||
                        attribute === 'elemento_id') {
                        convertedValue = Number(value);
                    }

                    const result = await updatePersonaAttribute(personaId, attribute, convertedValue.trim());
                }
            }

            showResult(personaResult, `Persona ID ${personaId} atualizada com sucesso!`);
        }
    } catch (error) {
        showResult(personaResult, `Erro: ${error.message}`);
    }
});

searchPersonaForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const action = event.submitter.getAttribute('data-action');
    const formData = new FormData(searchPersonaForm);

    try {
        const personaId = parseInt(formData.get('id_persona').trim());

        if (action === 'search') {
            const result = await getSpecificPersona(personaId);
            let resultString = `Persona encontrada: ${result.nome} (ID: ${result.id})\nOrigem: ${result.origem}\nPrimeira Aparição: ${result.primeira_aparicao}\nClasse: ${result.classe}\nNível Inicial: ${result.nivel_inicial}\nArcana: ${result.nome_arcana}\nElemento ID: ${result.nome_elemento}`;

            if (!result.classe) {
                resultString = `Persona encontrada: ${result.nome} (ID: ${result.id})\nOrigem: ${result.origem}\nPrimeira Aparição: ${result.primeira_aparicao}\nNível Inicial: ${result.nivel_inicial}\nArcana: ${result.nome_arcana}\nElemento ID: ${result.nome_elemento}`;
            }

            showResult(personaResult, resultString);
        } else if  (action === 'list') {
            const result = await getAllPersonas();
            let resultString = 'Lista de Personas:\n';

            result.forEach((persona) => {
                resultString += `- ${persona.nome} (ID: ${persona.id}) - ${persona.nome_arcana}\n`;
            });

            showResult(personaResult, resultString);
        } else if (action === 'verify') {
            if (personaId) {
                const result = await verifySpecificPersona(personaId);
                showResult(personaResult, `Verificação de Persona ID ${personaId}: ${result}`);
            } else {
                const result = await verifyPersona();
                showResult(personaResult, `Verificação de Personas: ${result}`);
            }
        }
    } catch (error) {
        showResult(personaResult, `Erro: ${error.message}`);
    }
});

deletePersonaForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const formData = new FormData(deletePersonaForm);

    try {
        const personaId = parseInt(formData.get('id_persona').trim());

        const result = await deletePersona(personaId);
        showResult(personaResult, `${result}`);
    } catch (error) {
        showResult(personaResult, `Erro: ${error.message}`);
    }
});

optionsButton.addEventListener('click', async (event) => {
    event.preventDefault();

    try {
        const result = await verifyPersonaOptions();
        showResult(personaResult, result)
    } catch (error)
    {
        showResult(personaResult, `Erro: ${error.message}`);
    }
});

elementsForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const action = event.submitter.getAttribute('data-action');
    const formData = new FormData(elementsForm);

    try {
        const elementId = parseInt(formData.get('id_elemento').trim());

        if(action === 'search') {
            const result = await getSpecificElement(elementId);
            showResult(elementsResult, `Elemento encontrado: ${result.nome} (ID: ${result.id})`);
        } else if (action === 'list') {
            const result = await getAllElements();
            let resultString = 'Lista de Elementos:\n';

            result.forEach((element) => {
                resultString += `- ${element.nome} (ID: ${element.id})\n`;
            });

            showResult(elementsResult, resultString);
        } else if (action === 'verify-options') {
            const result = await verifyElementsOptions();
            showResult(elementsResult, result)
        } else if (action === 'verify') {
            if (elementId) {
                const result = await verifySpecificElements(elementId);
                showResult(elementsResult, `Verificação de Elemento ID ${elementId}: ${result}`);
            } else {
                const result = await verifyElements();
                showResult(elementsResult, `Verificação de Elementos: ${result}`);
            }
        }
    } catch (error) {
        showResult(elementsResult, `Erro: ${error.message}`);
    }
});

arcanaForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const action = event.submitter.getAttribute('data-action');
    const formData = new FormData(arcanaForm);

    try {
        const arcanaId = parseInt(formData.get('id_arcano').trim());

        if(action === 'search') {
            const result = await getSpecificArcana(arcanaId);
            showResult(arcanasResult, `Arcana encontrado: ${result.nome} (ID: ${result.id})\n\n${result.descricao}`);
        } else if (action === 'list') {
            const result = await getAllArcanas();
            let resultString = 'Lista de Arcanas:\n';

            result.forEach((arcana) => {
                resultString += `- ${arcana.nome} (ID: ${arcana.id})\n`;
            });

            showResult(arcanasResult, resultString);
        } else if (action === 'verify-options') {
            const result = await verifyArcanasOptions();
            showResult(arcanasResult, result)
        } else if (action === 'verify') {
            if (arcanaId || arcanaId === 0) {
                const result = await verifySpecificArcana(arcanaId);
                showResult(arcanasResult, `Verificação de Arcana ID ${arcanaId}: ${result}`);
            } else {
                const result = await verifyArcanas();
                showResult(arcanasResult, `Verificação de Arcanas: ${result}`);
            }
        }
    } catch (error) {
        showResult(arcanasResult, `Erro: ${error.message}`);
    }
});