/**
 * Loads public game data from the server and populates the specified list element.
 * @param {string} listId The id of the list element to populate.
 * @returns {Promise<void>} A promise that resolves when the public game list is loaded.
 */
export function loadPublicGames(listId) {
    return fetch("/data/public-games")
        .then(response => response.json())
        .then(json => {
            const playerList = document.getElementById(listId);
            playerList.innerHTML = "";
            for (const name in json) {
                const info = json[name];
                const li = document.createElement("li");
                li.textContent = `${name}: Players: [${info.players.join(", ")}], Status: ${info.status}` 
                    + (info.status === "Finished" ? `, Winner: ${info.winner}` : "");
                playerList.appendChild(li);
            }
        });
}