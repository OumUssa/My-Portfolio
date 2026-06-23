<template>
  <section class="panel-layout">
    <div class="panel">
      <div class="panel-head">
        <div>
          <p class="eyebrow">Contacts</p>
          <h3>Contact Messages</h3>
        </div>
        <div class="panel-actions">
          <input
            v-model="search"
            class="search"
            type="search"
            placeholder="Search messages..." />
        </div>
      </div>

      <p v-if="loading" class="error-banner" style="border-color: #cbd5e1; background: #f8fafc; color: #475569;">Loading contacts...</p>
      <p v-if="error" class="error-banner">{{ error }}</p>

      <div class="table-container" v-if="!loading && !error">
        <div class="table-header">
          <div class="th-id" style="width: 60px;">#</div>
          <div class="th-info" style="flex: 2;">Sender</div>
          <div class="th-status" style="flex: 2;">Subject</div>
          <div class="th-actions" style="width: 120px;">Action</div>
        </div>

        <div class="list-stack">
          <button
            v-for="(contact, index) in filteredContacts"
            :key="contact.id || index"
            class="list-item"
            :class="{ selected: selectedContact?.id === contact.id }"
            @click="selectContact(contact)">
            
            <div class="td-id" style="width: 60px;">
              <span class="index-badge">{{ String(index + 1).padStart(3, '0') }}</span>
            </div>

            <div class="td-info" style="flex: 2;">
              <div class="info-text">
                <strong>{{ contact.name }}</strong>
                <small>{{ contact.email }}</small>
              </div>
            </div>

            <div class="td-status" style="flex: 2; color: #475569; font-size: 14px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
              {{ contact.subject }}
            </div>

            <div class="td-actions" style="width: 120px; justify-content: flex-end;">
              <button
                class="action-pill delete-pill"
                type="button"
                title="Delete message"
                @click.stop="handleDeleteContact(contact.id)">
                <i class="bi bi-trash3"></i> Delete
              </button>
            </div>
          </button>
        </div>
        
        <div v-if="!filteredContacts.length" class="detail-empty">
          <p>No contact messages found.</p>
        </div>
      </div>
    </div>

    <!-- Right Side Detail Panel -->
    <div class="panel detail-panel">
      <p class="eyebrow">Message Details</p>

      <div v-if="!selectedContact" class="detail-empty">
        <i class="bi bi-envelope"></i>
        <h3>Select a message</h3>
        <p>Click any row to read the full message here.</p>
      </div>

      <div v-else class="hp-card" style="padding: 24px;">
        <h3 class="hp-title" style="font-size: 20px; margin-bottom: 8px;">{{ selectedContact.subject }}</h3>
        <div style="display: flex; gap: 12px; align-items: center; margin-bottom: 24px; padding-bottom: 16px; border-bottom: 1px solid #e2e8f0;">
          <div style="width: 40px; height: 40px; border-radius: 50%; background: #eef2ff; color: #6366f1; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 16px; flex-shrink: 0;">
            {{ selectedContact.name ? selectedContact.name.charAt(0).toUpperCase() : 'U' }}
          </div>
          <div style="overflow: hidden;">
            <strong style="display: block; color: #0f172a; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{{ selectedContact.name }}</strong>
            <a :href="`mailto:${selectedContact.email}`" style="color: #6366f1; font-size: 13px; text-decoration: none; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; display: block;">{{ selectedContact.email }}</a>
          </div>
        </div>
        <div style="color: #334155; line-height: 1.6; font-size: 15px; white-space: pre-wrap;">
          {{ selectedContact.message }}
        </div>
        <div style="margin-top: 24px; padding-top: 16px; border-top: 1px solid #e2e8f0; display: flex; gap: 8px;">
          <a :href="`mailto:${selectedContact.email}?subject=Re: ${selectedContact.subject}`" class="hp-btn hp-edit" style="text-decoration: none;">
            <i class="bi bi-reply"></i> Reply
          </a>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import { fetchContacts, deleteContact } from "@/data/contactsApi.js";

const props = defineProps({
  token: {
    type: String,
    required: true,
  },
});

const contacts = ref([]);
const search = ref("");
const selectedContact = ref(null);
const loading = ref(true);
const error = ref("");

onMounted(async () => {
  try {
    loading.value = true;
    contacts.value = await fetchContacts(props.token);
  } catch (err) {
    error.value = "Failed to load contacts.";
  } finally {
    loading.value = false;
  }
});

const filteredContacts = computed(() => {
  const keyword = search.value.trim().toLowerCase();
  if (!keyword) return contacts.value;
  return contacts.value.filter((c) =>
    (c.name + " " + c.email + " " + c.subject).toLowerCase().includes(keyword)
  );
});

function selectContact(contact) {
  selectedContact.value = contact;
}

async function handleDeleteContact(id) {
  if (!confirm("Are you sure you want to delete this message?")) return;
  
  try {
    await deleteContact(id, props.token);
    contacts.value = contacts.value.filter((c) => c.id !== id);
    if (selectedContact.value?.id === id) {
      selectedContact.value = null;
    }
  } catch (err) {
    alert("Failed to delete contact.");
  }
}
</script>

<style scoped>
/* Re-use CreateTechStack / CreateProject UI styles */
.panel-layout {
  display: grid;
  grid-template-columns: 1fr 340px;
  gap: 24px;
  align-items: start;
}
.panel {
  padding: 24px;
  background: #fff;
  border-radius: 20px;
  border: 1px solid #e2e8f0;
  box-shadow: 0 4px 12px rgba(15, 23, 42, 0.02);
}
.panel-head {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 24px;
}
.eyebrow {
  margin: 0 0 8px;
  text-transform: uppercase;
  letter-spacing: 0.18em;
  font-size: 12px;
  color: #6366f1;
  font-weight: 700;
}
h3 { margin: 0; font-size: 20px; font-weight: 800; color: #1e293b; }
.panel-actions { display: flex; gap: 8px; }
.search { padding: 8px 14px; border: 1px solid #e2e8f0; border-radius: 8px; font-size: 14px; background: #f8fafc; outline: none; }
.search:focus { border-color: #6366f1; background: #fff; }

.table-container { display: flex; flex-direction: column; overflow-x: auto; }
.table-header { display: flex; align-items: center; padding: 0 16px 12px; font-size: 13px; font-weight: 600; color: #64748b; text-transform: uppercase; min-width: 600px; }
.list-stack { display: flex; flex-direction: column; gap: 10px; min-width: 600px; }
.list-item { display: flex; align-items: center; width: 100%; padding: 12px 16px; border-radius: 16px; border: 1px solid rgba(148, 163, 184, 0.18); background: #fff; text-align: left; transition: all 0.2s ease; cursor: pointer; }
.list-item:hover { border-color: #94a3b8; transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.05); }
.list-item.selected { border-color: #6366f1; box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.1); }
.td-id .index-badge { font-weight: 700; color: #6366f1; font-size: 13px; background: #e0e7ff; padding: 4px 8px; border-radius: 6px; }
.info-text strong { color: #0f172a; font-size: 14px; display: block; margin-bottom: 2px;}
.info-text small { color: #64748b; font-size: 12px; }
.td-actions { display: flex; gap: 6px; }
.action-pill { display: inline-flex; align-items: center; gap: 6px; padding: 6px 10px; border-radius: 8px; font-size: 12px; font-weight: 600; border: 1px solid rgba(148, 163, 184, 0.24); background: #fff; color: #475569; transition: all 0.2s ease; }
.action-pill:hover { background: #f8fafc; color: #0f172a; border-color: #cbd5e1; }
.delete-pill:hover { color: #dc2626; border-color: #fecaca; background: #fef2f2; }
.error-banner { margin: 1rem 0; padding: 1rem; border-radius: 12px; border: 1px solid #fca5a5; background: #fef2f2; color: #991b1b; font-weight: 600; }
.detail-empty { margin-top: 24px; display: flex; flex-direction: column; align-items: center; gap: 8px; color: #94a3b8; text-align: center; padding: 40px 20px; }
.detail-empty i { font-size: 40px; color: #cbd5e1; }
.hp-card { margin-top: 12px; border: 1px solid #f1f5f9; border-radius: 14px; overflow: hidden; background: #fff; box-shadow: 0 2px 12px rgba(0,0,0,0.04); }
.hp-btn { display: inline-flex; align-items: center; gap: 6px; padding: 7px 14px; border-radius: 8px; font-size: 12px; font-weight: 600; border: 1px solid rgba(148, 163, 184, 0.24); background: #fff; color: #475569; cursor: pointer; transition: all 0.2s ease; }
.hp-edit:hover { color: #16a34a; border-color: #bbf7d0; background: #f0fdf4; }

@media (max-width: 900px) {
  .panel-layout { grid-template-columns: 1fr; }
}
</style>
