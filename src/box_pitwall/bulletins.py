from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Bulletin:
    id: str
    author: str
    title: str
    body: str


BULLETINS: dict[str, Bulletin] = {
    bulletin.id: bulletin
    for bulletin in (
        Bulletin(
            id="race-direction-01",
            author="Direção de Prova",
            title="Limites de pista",
            body="Os limites de pista da curva 4 serão monitorados por câmera. "
            "Três infrações geram bandeira preta e branca.",
        ),
        Bulletin(
            id="weather-01",
            author="Meteorologia",
            title="Previsão do tempo",
            body="30% de chance fraca a partir da volta 30. "
            "Temperatura da pista estável em 41 ºC.",
        ),
    )
}
