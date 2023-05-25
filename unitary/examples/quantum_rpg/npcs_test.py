# Copyright 2023 The Unitary Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unitary.alpha as alpha
import unitary.examples.quantum_rpg.battle as battle
import unitary.examples.quantum_rpg.classes as classes
import unitary.examples.quantum_rpg.npcs as npcs


def test_observer():
    qar = npcs.Observer(name="glasses")
    c = classes.Analyst("cat")
    b = battle.Battle([c], [qar])
    assert qar.is_npc()
    assert qar.npc_action(b) == "Observer glasses measures cat at qubit cat_1"