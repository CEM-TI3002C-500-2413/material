-- Creando tabla de texto completo para la tabla de restaurantes

CREATE VIRTUAL TABLE "restaurants_fts" USING fts5 (
	"Name",
	"Food Type",
	"Details",
	"City",
	"State",
    content='restaurants',
    content_rowid='ID'
)

-- Insertando datos en la tabla de texto completo (FTS
INSERT INTO restaurants_fts ("Name", "Food Type", "Details", "City", "State") SELECT "Name", "Food Type", "Details", "City", "State" FROM restaurants;

-- Creando TRIGGERS para mantener la tabla de texto completo actualizada
CREATE TRIGGER restaurants_ai AFTER INSERT ON restaurants BEGIN
    INSERT INTO restaurants_fts (rowid, "Name", "Food Type", "Details", "City", "State") 
        VALUES (new."ID", new."Name", new."Food Type", new."Details", new."City", new."State");
END;

CREATE TRIGGER restaurants_ad AFTER DELETE ON restaurants BEGIN
    INSERT INTO restaurants_fts (restaurants_fts, rowid, "Name", "Food Type", "Details", "City", "State") 
        VALUES ('delete', old."ID", old."Name", old."Food Type", old."Details", old."City", old."State");
END;

CREATE TRIGGER restaurants_au AFTER UPDATE ON restaurants BEGIN
    INSERT INTO restaurants_fts (restaurants_fts, rowid, "Name", "Food Type", "Details", "City", "State") 
        VALUES ('delete', old."ID", old."Name", old."Food Type", old."Details", old."City", old."State");
    INSERT INTO restaurants_fts ("Name", "Food Type", "Details", "City", "State") 
        VALUES (new."Name", new."Food Type", new."Details", new."City", new."State");
END;

-- Probando la tabla de texto completo
SELECT * FROM restaurants_fts WHERE restaurants_fts MATCH 'Mexican' ORDER BY rank;