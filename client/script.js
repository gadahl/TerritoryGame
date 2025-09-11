/**
 * Loads player data from the server and populates the specified list element.
 * @param {string} listId The id of the list element to populate.
 * @returns {Promise<void>} A promise that resolves when the player list is loaded.
 */
export function loadPlayers(listId) {
    return fetch("/data/players")
        .then(response => response.json())
        .then(json => {
            const playerList = document.getElementById(listId);
            playerList.innerHTML = "";
            for (const name in json) {
                const info = json[name];
                const li = document.createElement("li");
                li.textContent = `${name} owns these territories: ${info.territories.join(", ")}`;
                playerList.appendChild(li);
            }
        });
}