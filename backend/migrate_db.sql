-- ============================================================
-- VidyaAi — Database Migration
-- Run this in Supabase SQL editor ONCE, then re-run the seeder.
-- ============================================================

-- 1. Add new columns
ALTER TABLE questions
    ADD COLUMN IF NOT EXISTS exam            VARCHAR(50),
    ADD COLUMN IF NOT EXISTS question_number INTEGER,
    ADD COLUMN IF NOT EXISTS question_en     TEXT,
    ADD COLUMN IF NOT EXISTS question_hi     TEXT,
    ADD COLUMN IF NOT EXISTS source_pdf      VARCHAR(500);

-- 2. Backfill new columns from old ones
UPDATE questions
    SET question_en = question_text
    WHERE question_en IS NULL AND question_text IS NOT NULL;

UPDATE questions
    SET question_hi = question_text_hi
    WHERE question_hi IS NULL AND question_text_hi IS NOT NULL;

-- 3. Make question_en NOT NULL (safe after backfill above)
ALTER TABLE questions
    ALTER COLUMN question_en SET NOT NULL;

-- 4. Drop NOT NULL from old columns that new pipeline no longer fills
--    (critical — new inserts don't include these fields)
ALTER TABLE questions
    ALTER COLUMN question_text   DROP NOT NULL,
    ALTER COLUMN correct_answer  DROP NOT NULL,
    ALTER COLUMN difficulty      DROP NOT NULL,
    ALTER COLUMN explanation     DROP NOT NULL,
    ALTER COLUMN phase           DROP NOT NULL;

-- 5. Widen option columns from VARCHAR(300) to TEXT
--    (real-world options can exceed 300 chars in bilingual PDFs)
ALTER TABLE questions
    ALTER COLUMN option_a TYPE TEXT,
    ALTER COLUMN option_b TYPE TEXT,
    ALTER COLUMN option_c TYPE TEXT,
    ALTER COLUMN option_d TYPE TEXT;

-- 5. Create processed_files table (PDF hash tracking)
CREATE TABLE IF NOT EXISTS processed_files (
    id           SERIAL PRIMARY KEY,
    file_name    VARCHAR(500) NOT NULL,
    file_hash    VARCHAR(64)  NOT NULL UNIQUE,
    processed_at TIMESTAMPTZ  NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS ix_processed_files_file_hash ON processed_files (file_hash);

-- ============================================================
-- Optional cleanup — uncomment and run ONLY after verifying
-- everything works with the new schema.
-- ============================================================
-- ALTER TABLE questions DROP COLUMN IF EXISTS question_text;
-- ALTER TABLE questions DROP COLUMN IF EXISTS question_text_hi;
-- ALTER TABLE questions DROP COLUMN IF EXISTS subject_code;
-- ALTER TABLE questions DROP COLUMN IF EXISTS phase;
-- ALTER TABLE questions DROP COLUMN IF EXISTS image_url;
-- ALTER TABLE questions DROP COLUMN IF EXISTS explanation;
-- ALTER TABLE questions DROP COLUMN IF EXISTS explanation_hi;
-- ALTER TABLE questions DROP COLUMN IF EXISTS option_a_hi;
-- ALTER TABLE questions DROP COLUMN IF EXISTS option_b_hi;
-- ALTER TABLE questions DROP COLUMN IF EXISTS option_c_hi;
-- ALTER TABLE questions DROP COLUMN IF EXISTS option_d_hi;
