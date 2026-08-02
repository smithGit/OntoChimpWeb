/* msqlt07_create_term_model_doc.sql Table creation script */

CREATE TABLE term_model_doc
(
    id INT NOT NULL AUTO_INCREMENT,
    term_id VARCHAR(12),
    model_id VARCHAR(10) NOT NULL,
	  doc_id VARCHAR(10) NOT NULL,
    term_norm VARCHAR(90) NOT NULL,
    PRIMARY KEY (id)
)


more complete version with timestamp:

CREATE TABLE term_model_doc (
    id INT AUTO_INCREMENT PRIMARY KEY,
    term_id VARCHAR(64) NOT NULL,
    model_id VARCHAR(64) NOT NULL,
    doc_id VARCHAR(64) NOT NULL,
    term_norm VARCHAR(255) NOT NULL,
    head VARCHAR(255),
    domain VARCHAR(255),
    sub_domain VARCHAR(255),
    kc_count INT NOT NULL DEFAULT 0,
    cl_tmd_id VARCHAR(64),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
 >> TODO contrast with using DATETIME instead... see what the diff is